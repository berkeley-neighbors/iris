import os
import subprocess
import socket
import sys
import time

dbpath = os.environ.get('DATABASE_PATH', '/home/iris/db')

def load_sqldump(config, sqlfile, one_db=True):
    print('Importing %s...' % sqlfile)
    effective_port = 3306
    if 'port' in config:
        effective_port = config['port']
    with open(sqlfile) as h:
        cmd = ['/usr/bin/mysql', '-h', config['host'], '-u',
               config['user'], '-p' + config['password'], '-P' + str(effective_port)]
        if one_db:
            cmd += ['-o', config['database']]
        proc = subprocess.Popen(cmd, stdin=h)
        proc.communicate()

        if proc.returncode == 0:
            print('DB successfully loaded ' + sqlfile)
            return True
        else:
            print(('Ran into problems during DB bootstrap. '
                   'IRIS will likely not function correctly. '
                   'mysql exit code: %s for %s') % (proc.returncode, sqlfile))
            return False

def wait_for_mysql(config):
    print('Checking MySQL liveness on %s...' % config['host'])

    effective_port = 3306
    if 'port' in config:
        effective_port = config['port']

    db_address = (config['host'], effective_port)
    tries = 0
    while True:
        try:
            sock = socket.socket()
            sock.connect(db_address)
            sock.close()
            break
        except socket.error:
            if tries > 20:
                print('Waited too long for DB to come up. Bailing.')
                sys.exit(1)

            print('DB not up yet. Waiting a few seconds..')
            time.sleep(2)
            tries += 1
            continue