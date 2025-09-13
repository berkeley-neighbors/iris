import os
import sys
from glob import glob
from iris.config import load_config
from sql import load_sqldump, dbpath, wait_for_mysql

def initialize_mysql_schema(config):
    print('Seeding Iris database with database')

    re = load_sqldump(config, os.path.join(dbpath, 'dummy_data.sql'))
    if not re:
        sys.stderr.write('Failed to load dummy data.')


def main():
    iris_config = load_config(
        os.environ.get('IRIS_CFG_PATH', '/home/iris/config/config.yaml'))
    mysql_config = iris_config['db']['conn']['kwargs']

    initialize_mysql_schema(mysql_config)


if __name__ == '__main__':
    main()