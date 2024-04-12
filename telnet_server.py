#!/usr/bin/env python3

import socket, sys, threading
from imports.logger import logger
from imports.console import *
from imports.color_strings import color_strings
#from playground import fileUploader

def handle_client(client_socket, client_address):
    #telnet_options = bytes([255, 254, 1, 255, 251, 34])
    client_socket.sendall(b'\xff\xfc\x01\xff\xfb\x22') # WONT ECHO, WILL LINEMODE
    t = client_socket.recv(1024)  
    telnet_negotiation = client_socket.recv(1024)
#    print(t)
#    print(telnet_negotiation)
    client_socket.send(color_strings.get('welcome').encode('utf-8'))
    client_socket.send(color_strings.get('help').encode('utf-8'))
    curr_env = 'Basics'
    test = "\033[1m\033[32m"+curr_env+"\033[0m\033[32m[C4D]\033[0m\033[1m\033[32m>\033[0m "
    client_socket.send(test.encode('utf-8'))
#    print("before while loop")
    while True:
        try:
            command = client_socket.recv(1024).rstrip().decode().lower()
            # Log command
#            print("command has been received")
            logger(client_address[0], client_address[1], command)
            if (command in color_strings):
                client_socket.send(color_strings.get(command).encode('utf-8'))

            elif (command == 'exit' or command == 'reboot'):
                break

            elif (command.startswith('/bin/busybox')):
                    busyboxer(command, client_socket)

            elif (not is_valid_command(command)):
                client_socket.send(b"Currently unavailable or not a valid command\n")

            else:
                retrieve_response(command, client_socket, client_address)

            curr_env = environment_switcher(client_socket, command, curr_env)
            test2 = "\033[1m\033[32m"+curr_env+"\033[0m\033[32m[C4D]\033[0m\033[1m\033[32m>\033[0m "
            client_socket.send(test2.encode('utf-8'))

        except Exception as e:
#            print(f"Error: {e}")
            break
    client_socket.close()

def main():
    host = '0.0.0.0'  # Listen on all available network interfaces
    port = 23
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
#    print(f"[*] Listening on {host}:{port}")
    
    try:
        while True:
            client_socket, client_address = server_socket.accept()
#            print(f"[*] Accepted connection from {client_address[0]}:{client_address[1]}")
            
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()

    except Exception as e:
#        print("\n[*] Exiting...\n")
#        print(f"Exception: {e}")
        server_socket.close()
        sys.exit()

if __name__ == "__main__":
    main()

