"""
    PYCOM
    Made by Monnapse
    Create terminal commands the easiest way.

    0.4.1
"""

import sys
import inspect

commands = []

class NoneType:
    def __init__(self):
        self.__type__ = None

def command(function):
    commands.append(function)

def get_param_pos(param_str, param_dict):
    index = 0
    for param in param_dict:
        if param == param_str:
            return index
        index += 1

def error(msg: str):
    print(f"Lime Encountered and error: {msg}")

def r_cmd(args):
    args.pop(0)
    function_name = args.pop(0)

    arguments = []

    for arg in args:
        if str.startswith(arg, "--"):
            long_option = str.split(arg, "--")
            arguments.append([long_option[1], True])
        else:
            arg_list = arg.split("=")
            if len(arg_list) == 1:
                arg_list.insert(0, None)
            arguments.append(arg_list)

    for f in commands:
        if f.__name__ == function_name:
            new_args = []
            param_dict = inspect.signature(f).parameters
            has_eqaul = False

            for arg in arguments:
                arg_name = arg[0]
                arg_value = arg[1]

                assigner = False

                if arg_name != None:
                    has_eqaul = True

                    index = get_param_pos(arg_name, param_dict)
                    if index == None:
                        error(f"'{arg_name}' is not a param.")
                        return
                    
                    try:
                        if new_args[index] != None:
                            assigner = True
                            new_args[index] = arg_value
                    except:
                        differrence = index - len(new_args)
                        for i in range(differrence):
                            new_args.append(NoneType())

                elif not arg_name and has_eqaul:
                    error(f"If you assign parameter you must end with assign")
                    return
                if assigner == False:           
                    new_args.append(arg_value)

            # Unload new_arg list, basically take classes and return __type__
            for arg in new_args:
                if isinstance(arg, NoneType):
                    new_args[new_args.index(arg)] = arg.__type__

            f(*tuple(new_args))
            break

def start():
    r_cmd(sys.argv)