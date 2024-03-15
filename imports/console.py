#!/usr/bin/env python3

from os.path import exists

class bcolors:
    PURPLE = '\033[1m\033[35m'
    BLUE = '\033[36m'
    YELLOW = '\033[33m'
    RED = '\033[1m\033[31m'
    B_GREEN = '\033[1m\033[32m'
    D_GREEN = '\033[32m'
    ENDC = '\033[0m'

command_path = '/home/ubuntu/Masters/command_data/'

def is_valid_command(command):
    if exists(command_path + command):
        return True
    return False

def welcome(client_socket):
	client_socket.send(b"""
\033[1m\033[35mWelcome on console

""")

def help(client_socket):
    client_socket.send(b"""
\033[0m\033[1m\033[31mHelp :
\033[0m\033[36mcmd \033[0m\033[33m[option1|option2]{string}(number) \033[0m

\033[1m\033[31mBuiltins :
\033[0m\033[36mcversion \033[0m\033[33m \033[0m          Console version
\033[36mhelp \033[0m\033[33m \033[0m              Display help
\033[36mscreen \033[0m\033[33m[(X)] \033[0m       Change to screen X. If no argument, display screen list
\033[36mcolor \033[0m\033[33m[0|1] \033[0m        Enable/Disable color output
\033[36mlang \033[0m\033[33m[{str}] \033[0m       Set the console language
\033[36mreboot \033[0m\033[33m[(waitTime)] \033[0mReboot
\033[36mcompletion \033[0m\033[33m \033[0m        Activate advanced completion
\033[36mexit \033[0m\033[33m \033[0m              Quit

\033[1m\033[31mBasics :
\033[0m\033[36m1wire \033[0m\033[33m \033[0m             Display 1wire information
\033[36miostate \033[0m\033[33m \033[0m           Display input/output state
\033[36mmodem \033[0m\033[33m \033[0m             Display modem state
\033[36mgpspos \033[0m\033[33m \033[0m            Retrieve last GPS position
\033[36mlist \033[0m\033[33m[all|{module}][dl] \033[0mList available modules.
                    [all] List all available modules parameters.
                    [module] List available module parameters.
                    [dl] Download result.
\033[36mg \033[0m\033[33m{module} {parameter} [(index)] \033[0mGet module parameter value
\033[36ms \033[0m\033[33m{module} {parameter} [(index)] {value} \033[0mSet module parameter value
\033[36mlistdb \033[0m\033[33m \033[0m            List available DB parameters
\033[36mgdb \033[0m\033[33m{name} \033[0m         Get a DB parameter
\033[36msdb \033[0m\033[33m{name} {value} \033[0m Set a DB parameter
\033[36mlog \033[0m\033[33m[print|debug|warn|error|{str}] \033[0mDisplay last log
\033[36mlogdump \033[0m\033[33m[print|debug|warn|error|{str}] \033[0mDisplay all logs
\033[36mconfigure \033[0m\033[33m \033[0m         Upload a new conf file
Segmentation fault (core dumped)
Error code: 11
Memory address: 0x7fff3b9645d8
Stack trace:
    1. main() at /usr/bin/update
    2. getPermission() at /home/user/updater/mdi.UpdateHandler:141
""")


def screen(client_socket):
    client_socket.send(b"""
\033[36mscreen 0\033[0m    Basics
\033[36mscreen 1\033[0m    Advanced
\033[36mscreen 2\033[0m    Commands
""")


def screen_1(client_socket):
    client_socket.send(b"""
\033[1m\033[31mAdvanced :
\033[0m\033[36mip \033[0m\033[33m[{str}] \033[0m         Display all ip addresses. If str, display only str address.
\033[36mstats \033[0m\033[33m \033[0m             Display stats.
\033[36mllog \033[0m\033[33m[soft|gps|update|kstart|mAT|mPPP] \033[0mDisplay last logs of:
                                           software, gps, kernel start, modem AT, or modem PPP
\033[36mskey \033[0m\033[33m[update|delete] \033[0mUpdate|Delete server key
\033[36mukey \033[0m\033[33m[update|delete] \033[0mUpdate|Delete user key
\033[36mlogs \033[0m\033[33m[get|delete][all|{filename}|crashes] \033m[0mRetrieve or Delete logs of software
\033[36mstopsoft \033[0m\033[33m \033[0m          Stop the software
\033[36musercpn \033[0m\033[33m[list|start|stop|remove][all|{cpnName}] \033[0mList user components
\033[36mgprsupdate \033[0m\033[33m[start|stop] \033[0mEnable / Disable GRPS update
\033[36mgeomap \033[0m\033[33m[update|delete] \033[0mUpdate / Delete a geofencing map
\033[36mupdate \033[0m\033[33m \033[0m            Upload an update package
\033[36mrestore \033[0m\033[33m[all|write|pdm|db|user] \033[0mRestore parameters of write, db or pbm
\033[36mrestoreFull \033[m\033[33m \033[0m        Restore device to the initial configuration state
\033[36version \033[m\033[33m \033[0m             Display software/hardware version
\033[36mremote \033[m\033[33m[{ip}] \033[0m       Console on remote device
\033[36mcpu \033m[m\033[33m[{cpnName}] \033[0m    Get CPU usage for group
""") 




def retrieve_response(command, client_socket, client_address):
    if command:
        with open(command_path + command, 'rb') as f:
            f_content = f.read()
        client_socket.send(f_content)
    else:
        print("No command was provided by the client")

