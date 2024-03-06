#!/usr/bin/env python3

class bcolors:
    PURPLE = '\033[1m\033[35m'
    BLUE = '\033[36m'
    YELLOW = '\033[33m'
    RED = '\033[1m\033[31m'
    B_GREEN = '\033[1m\033[32m'
    D_GREEN = '\033[32m'
    ENDC = '\033[0m'

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


""")