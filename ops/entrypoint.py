# Copyright (c) LinkedIn Corporation. All rights reserved. Licensed under the BSD-2 Clause license.
# See LICENSE in the project root for license information.

import os
import sys
from glob import glob
from iris.config import load_config
from db.sql import load_sqldump, dbpath, wait_for_mysql

initializedfile = os.environ.get('INIT_FILE', '/home/iris/db_initialized')

def initialize_mysql_schema(config):
    print('Initializing Iris database')
    # disable one_db to let schema_0.sql create the database
    re = load_sqldump(config, os.path.join(dbpath, 'schema_0.sql'), one_db=False)
    if not re:
        sys.exit('Failed to load schema into DB.')

    for f in glob(os.path.join(dbpath, 'patches', '*.sql')):
        re = load_sqldump(config, f)
        if not re:
            sys.exit('Failed to load DB patche: %s.' % f)

    with open(initializedfile, 'w'):
        print('Wrote %s so we don\'t bootstrap db again' % initializedfile)


def main():
    iris_config = load_config(
        os.environ.get('IRIS_CFG_PATH', '/home/iris/config/config.yaml'))
    mysql_config = iris_config['db']['conn']['kwargs']

    # It often takes several seconds for MySQL to start up. iris dies upon start
    # if it can't immediately connect to MySQL, so we have to wait for it.
    wait_for_mysql(mysql_config)

    if os.environ.get('DOCKER_DB_BOOTSTRAP') != '0':
        if not os.path.exists(initializedfile):
            initialize_mysql_schema(mysql_config)

    os.execv('/usr/bin/uwsgi',
             # first array element is ARGV0, since python 3.6 it cannot be empty, using space
             # https://bugs.python.org/issue28732
             ['/usr/bin/uwsgi', '--yaml', '/home/iris/daemons/uwsgi.yaml:prod'])


if __name__ == '__main__':
    main()
