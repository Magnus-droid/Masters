#!/usr/bin/env python3

import socket
import sys
import threading
from logger import logger

def handle_client(client_socket, client_address):
    # Discard initial data (e.g., Telnet negotiation strings)
    initial_data = client_socket.recv(1024)
    print(initial_data)
    # Welcome message
    client_socket.send(b"""
\033[1m\033[31mHelp :
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
                    [dl] Download results.
\033[36mg \033[0m\033[33m{module} {parameter} [(index)] \033[0mGet module parameter value
\033[36ms \033[0m\033[33m{module} {parameter} [(index)] {value} \033[0mSet module parameter value
\033[36mlistdb \033[0m\033[33m \033[0m            List available DB parameters
\033[36mgdb \033[0m\033[33m{name} \033[0m         Get a DB parameter
\033[36msdb \033[0m\033[33m{name} {value} \033[0m Set a DB parameter
\033[36mlog \033[0m\033[33m[print|debug|warn|error|{str}] \033[0mDisplay last log
\033[36mlogdump \033[0m\033[33m[print|debug|warn|error|{str}] \033[0mDisplay all logs
\033[36mconfigure \033[0m\033[33m \033[0m         Upload a new conf file


    """)
    client_socket.send(b"Enter your username: ")
    username = client_socket.recv(1024).rstrip().decode()  # Convert bytes to string
    print(username)
    client_socket.send(b"Enter your password: ")
    password = client_socket.recv(1024).rstrip().decode()  # Convert bytes to string
    print(password)
    # Check credentials
    while username != "admin" or password != "password":
        client_socket.send(b"Username or password incorrect! Please try again.\n")
        client_socket.send(b"Enter your username: ")
        username = client_socket.recv(1024).rstrip().decode()  # Convert bytes to string
        print(username)
        client_socket.send(b"Enter your password: ")
        password = client_socket.recv(1024).rstrip().decode()  # Convert bytes to string
        print(password)
    client_socket.send(b"\nLogin successful!\n")
    client_socket.send(b"Available commands: version, help, quit\n")

    while True:
        client_socket.send(b"\nEnter command: ")
        command = client_socket.recv(1024).rstrip().decode().lower()  # Convert bytes to string
        
        # Log command
        logger(client_address[0], client_address[1], command)
        
        # Execute command
        if command == "version":
            client_socket.send(b"v1.2\n")
        elif command == "help":
            client_socket.send(b"Available commands:\n- 'help' \n- 'version' \n- 'quit' \n")
        elif command == "quit":
            client_socket.send(b"Goodbye!\n")
            break
        else:
            client_socket.send(b"Invalid command. Type 'help' for a list of available commands..\n")
    client_socket.close()

def main():
    host = '0.0.0.0'  # Listen on all available network interfaces
    port = 23
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    print(f"[*] Listening on {host}:{port}")
    
    try:
        while True:
            client_socket, client_address = server_socket.accept()
            print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
            
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()

    except KeyboardInterrupt:
        print("\n[*] Exiting...")
        server_socket.close()
        sys.exit()

if __name__ == "__main__":
    main()

