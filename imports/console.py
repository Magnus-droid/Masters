#!/usr/bin/env python3

from os.path import exists
from imports.color_strings import color_strings 


class bcolors:
    PURPLE = '\033[1m\033[35m'
    BLUE = '\033[36m'
    YELLOW = '\033[33m'
    RED = '\033[1m\033[31m'
    B_GREEN = '\033[1m\033[32m'
    D_GREEN = '\033[32m'
    ENDC = '\033[0m'

command_path = '/home/ubuntu/Masters/command_data/'


def environment_switcher(client_socket, command, curr_env):
    if command == 'screen 0':
        curr_env = 'Basics'
    elif command == 'screen 1':
        curr_env = 'Advanced'
    elif command == 'screen 2':
        curr_env = 'Commands'
    else:
        curr_env = curr_env
    return curr_env


def is_valid_command(command):
    if command in color_strings:
        return True
    elif exists(command_path + command):
        return True
    return False

def retrieve_response(command, client_socket, client_address):
    if command:
        with open(command_path + command, 'rb') as f:
            f_content = f.read()
        client_socket.send(f_content)
    else:
        print("No command was provided by the client")

