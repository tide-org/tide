# -*- coding: utf-8 -*-
'''
    __init__.py
'''

from .tide import Tide
import argparse
import os

def main():
    '''
       Main entrypoint for the cli application
    '''

    parser = argparse.ArgumentParser(description='Tide. From Text to Integrated Development Environment.')
    parser.add_argument('-c', '--config', help='The path of the config file')
    parser.add_argument('-a', '--args', help='A string of command arguments to be sent to Tide on first startup.')
    args = vars(parser.parse_args())
    arg_string = ''

    if args['config']:
        os.environment["TIDE_CONFIG_LOCATION"] = args['config'] 

    if args['args']:
        arg_string = args['args']

    tide = Tide()
    tide.start(arg_string)
