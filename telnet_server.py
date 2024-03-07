#!/usr/bin/env python3

import socket
import sys
import threading
from logger import logger
from console import retrieve_response, help, welcome, is_valid_command


def handle_client(client_socket, client_address):
    # Discard initial data (e.g., Telnet negotiation strings)
    telnet_negotiation = client_socket.recv(1024)
    print(telnet_negotiation)
    # Welcome message
    welcome(client_socket)
    help(client_socket)

    while True:
        client_socket.send(b"\033[1m\033[32mBasics\033[0m\033[32m[C4D]\033[0m\033[1m\033[32m>\033[0m ")
        command = client_socket.recv(1024).rstrip().decode().lower()  # Convert bytes to string
        # Log command
        logger(client_address[0], client_address[1], command)

        if (command == 'help'):
            help(client_socket)

        elif (command == 'exit'):
            break

        elif (not is_valid_command(command)):
            client_socket.send(b"Not a valid command\n")

        else:
            retrieve_response(command, client_socket, client_address)

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

