#!/usr/bin/env python3

import socket, sys, threading
from imports.logger import logger
from imports.console import *
from imports.color_strings import color_strings


def handle_client(client_socket, client_address):

    client_socket.sendall(b'\xff\xfc\x01\xff\xfb\x22') # WONT ECHO, WILL LINEMODE
    t = client_socket.recv(1024)  
    telnet_negotiation = client_socket.recv(1024)
    client_socket.send(color_strings.get('welcome').encode('utf-8'))
    client_socket.send(color_strings.get('help-cloud').encode('utf-8'))

    while True:

        client_socket.send(color_strings.get('line_start').encode('utf-8'))
        try:
            command = client_socket.recv(1024).rstrip().decode().lower()
            logger(client_address[0], client_address[1], command)

            if (command in color_strings):
                client_socket.send(color_strings.get(command).encode('utf-8'))
            elif (command == 'exit'):
                break

            elif (not is_valid_command(command)):
                client_socket.send(b"Not a valid command\n")

            else:
                retrieve_response(command, client_socket, client_address)


        except Exception as e:
            break
    client_socket.close()

def main():
    host = '0.0.0.0'
    port = 23
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    
    try:
        while True:

            client_socket, client_address = server_socket.accept()
            client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
            client_thread.start()

    except Exception as e:
        server_socket.close()
        sys.exit()

if __name__ == "__main__":
    main()

