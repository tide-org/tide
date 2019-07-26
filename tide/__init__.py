# -*- coding: utf-8 -*-
'''
    __init__.py
'''

import os
from os.path import dirname, abspath, join
import argparse
from argparse import RawTextHelpFormatter
from .tide import Tide
from .config import Config

def call_on_startup_functions(tide):
    pass

def check_update_buffers(command):
    pass

def run_config_command(tide, command):
    tide.run_config_command(command)
    print("config command ran successfully: " + command)
    check_update_buffers(command)

def run_startup_commands(tide, position):
    if "events" in Config().get():
        startup_commands = Config().get()["events"].get(position + "_startup", [])
        for startup_command in startup_commands:
            run_config_command(tide, startup_command)

def main():
    '''
       Main entrypoint for the cli application
    '''

    parser = argparse.ArgumentParser(
        description='Tide - From Text editor to Integrated Development Environment',
        formatter_class=RawTextHelpFormatter
    )
    parser.add_argument('-c', '--config',
        help='The path to the Tide Config file(s).',
        metavar=('config'),
        required=False
    )
    parser.add_argument('-a', '--arguments',
        help="A quoted string of arguments to pass \n" \
             "to Tide on startup.\n" \
             "e.g. tide -a \'test.exe 1 2 3\'",
        metavar=('args'),
        required=False
    )
    parser.add_argument('-v','--variables',
        action='append',
        nargs=2,
        metavar=('key','value'),
        help="Used to specify config variables to be\n" \
             "added/replaced to the configuration.\n" \
             "Can be called multiple times.\n" \
             "Config key names can be dot-chained.\n" \
             "e.g. `-v settings.editor.name stdio`\n",
        required=False
    )
    args = vars(parser.parse_args())
    tide_args = ''

    if args["config"]:
        os.environ["TIDE_CONFIG_LOCATION"] = args["config"]

    if args["arguments"]:
        tide_args = args["arguments"]
    
    print("tide config location: " + os.environ.get("TIDE_CONFIG_LOCATION"))
    if args["variables"]:
        print("Additional config variables: " + str(args["variables"]))
    print("initialising Tide...")
    tide = Tide()
    print("staring Tide with arguments: \'" + tide_args + "\'...")
    tide.start(tide_args)
    call_on_startup_functions(tide)
    run_startup_commands(tide, "after")
    print("exiting Tide CLI.")
