#!/usr/bin/env python3

import socket
import sys
import threading
from logger import logger
from console import retrieve_response, help


def handle_client(client_socket, client_address):
    # Discard initial data (e.g., Telnet negotiation strings)
    telnet_negotiation = client_socket.recv(1024)
    print(telnet_negotiation)
    # Welcome message
    retrieve_response('help', client_socket, client_address)
    retrieve_response('iostate', client_socket, client_address)
    retrieve_response('cversion', client_socket, client_address)
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

