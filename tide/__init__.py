import os
from time import sleep
import argparse
from argparse import RawTextHelpFormatter
from threading import Thread
import asyncio
from .tide import Tide
from .config import Config

def start_loop_seconds(loop, timeout_seconds):
    future = asyncio.wait_for(loop.run_in_executor(None, sleep, timeout_seconds), None)
    loop.run_until_complete(future)

def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

def start_new_loop(timeout_seconds):
    new_loop = asyncio.new_event_loop()
    if not timeout_seconds:
        thread = Thread(target=start_loop, args=(new_loop, ))
    else:
        thread = Thread(target=start_loop_seconds, args=(new_loop, timeout_seconds, ))
    thread.start()

def parse_args():
    parser = argparse.ArgumentParser(description='Tide - From Text editor to Integrated Development Environment', formatter_class=RawTextHelpFormatter)
    parser.add_argument('-c', '--config', help='The path to the Tide Config file(s).', metavar=('config'), required=False)
    parser.add_argument('-e', '--editor', help='The name of the edotor wrapper to target.', metavar=('editor'), required=False)
    parser.add_argument('-t', '--timeout', help="A timeout value in seconds to specify for how long\nthe main thread will stay alive for. If not specified,\nwill default to infinite.", metavar=('timeout'), required=False)
    parser.add_argument('-a', '--arguments', help="A quoted string of arguments to pass \nto Tide on startup.\ne.g. tide -a \'test.exe 1 2 3\'", metavar=('args'), required=False)
    parser.add_argument('-v','--variables', action='append', nargs=2, metavar=('key','value'), help="Used to specify config variables to be\nadded/replaced to the configuration.\nCan be called multiple times.\nConfig key names can be dot-chained.\ne.g. `-v settings.editor.name stdio`\n", required=False)
    return parser.parse_args()

def main():
    args = parse_args()
    if args.config:
        os.environ['TIDE_CONFIG_LOCATION'] = args.config
    start_new_loop(int(args.timeout or 0))
    tide = Tide(args.editor or '')
    tide.start()
