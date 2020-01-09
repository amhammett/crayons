import logging
import os
from argparse import ArgumentParser

logger = logging.getLogger('mfn')
logger.setLevel(logging.INFO)

FEATURE_GENERATE_MAKEFILE = True
FEATURE_PROJECT_INIT = True

HOME_DIR = os.getenv('HOME')
PWD_DIR = os.getenv('PWD')
LOG_CONFIG_PATH = '{}/mfn.log'.format(HOME_DIR)

logging.basicConfig(filename=LOG_CONFIG_PATH)
logger_stdout = logging.StreamHandler()
logger_stdout.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
logging.getLogger().addHandler(logger_stdout)

project_language = 'todo'  # todo

if (os.getenv('VERBOSE', False)):
    logger.setLevel(logging.DEBUG)


def colors_get_current():
    pass


def colors_list():
    pass


def colors_set_default():
    pass


def colors_set():
    pass


def parse_arguments(args=None):
    parser = ArgumentParser()
    parser.add_argument('--list', action='store_true', help='list the current display options')
    parser.add_argument('--set', help='set the current display settings')
    parser.add_argument('--get', action='store_true', help='get the current display settings')
    parser.add_argument('--default', action='store_true', help='default display settings')

    return parser.parse_args(args)


def main():
    args = parse_arguments()

    if (args.list):
        colors_list()

    if (args.get):
        colors_get_current()

    if (args.default):
        colors_set_default()

    if (args.set):
        colors_set(args.set)


if __name__ == '__main__':
    main()
