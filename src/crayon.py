import json
import logging
import os
import subprocess
from argparse import ArgumentParser

logger = logging.getLogger('mfn')
logger.setLevel(logging.INFO)

FEATURE_GENERATE_MAKEFILE = True
FEATURE_PROJECT_INIT = True

DEFAULT_DISPLAY_REFERENCE = 1
HOME_DIR = os.getenv('HOME')
PWD_DIR = os.getenv('PWD')
SRC_DIR = os.path.dirname(os.path.realpath(__file__))
LOG_CONFIG_PATH = '{}/crayon.log'.format(HOME_DIR)

logging.basicConfig(filename=LOG_CONFIG_PATH)
logger_stdout = logging.StreamHandler()
logger_stdout.setFormatter(logging.Formatter(logging.BASIC_FORMAT))
logging.getLogger().addHandler(logger_stdout)

project_language = 'todo'  # todo

if (os.getenv('VERBOSE', False)):
    logger.setLevel(logging.DEBUG)


def osascript_terminal(command_string):
    prepared_command_string = ' '.join([
        'osascript',
        '-e \'tell application "Terminal" to {}\''.format(command_string),
    ])
    logging.info(prepared_command_string)
    print(prepared_command_string)
    subprocess.run(prepared_command_string, shell=True)


def colors_get_current(display_ref=DEFAULT_DISPLAY_REFERENCE):
    osascript_terminal('"get current settings of window {}"'.format(display_ref))


def colors_list():
    for color in colors_list_get():
        print(color)


def colors_set_default():
    colors_set('default')


def colors_set(target_color_name, display_ref=DEFAULT_DISPLAY_REFERENCE):
    colors = colors_list_get()
    color_id = colors[target_color_name]['id']
    osascript_terminal('set current settings of window {} to settings set {}'.format(display_ref, color_id))


def colors_list_get():
    with open('{}/../data/colors.json'.format(SRC_DIR)) as colors_json:
        colors = json.load(colors_json)
        return colors['colors']


def parse_arguments(args=None):
    parser = ArgumentParser()
    parser.add_argument('--list', action='store_true', help='list the current display options')
    parser.add_argument('--set', help='set the current display settings')
    parser.add_argument('--target', help='specify the target terminal to interact with')
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
