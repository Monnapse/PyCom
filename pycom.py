"""
    PYCOM
    Made by Monnapse
    Create terminal commands the easiest way.

    0.1.0
"""

import sys

commands = []

def command(function):
    commands.append(function)

def r_cmd(args):
    args.pop(0)
    function_name = args.pop(0)
    for f in commands:
        if f.__name__ == function_name:
            f(*tuple(args))
            break

def start():
    r_cmd(sys.argv)