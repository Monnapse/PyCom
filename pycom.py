"""
    PYCOM
    Made by Monnapse
    Create terminal commands the easiest way.

    0.2.0
"""

import sys

commands = []

def command(function):
    commands.append(function)

def r_cmd(args):
    args.pop(0)
    function_name = args.pop(0)

    arguments = []
    long_options = []

    for arg in args:
        if str.startswith(arg, "--"):
            long_options.append(arg)
        else:
            arguments.append(arg)

    for f in commands:
        if f.__name__ == function_name:
            f(*tuple(arguments))
            break

def start():
    r_cmd(sys.argv)