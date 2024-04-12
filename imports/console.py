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

def file_transfer_handler(command):

    ##TODO
    pass


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



def busyboxer(command, client_socket):
    components = command.split(' ')
    if len(components) > 1:
        bb_command = components[1:]
        bb_response = f"{bb_command}: applet not found\n"
        client_socket.send(bb_response.encode('utf-8'))
    else:
        with open('/home/ubuntu/Masters/command_data/fake_busy_box', 'rb') as f:
            f_content = f.read()
        client_socket.send(f_content)



