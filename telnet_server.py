import socket
import sys
from logger import logger

def handle_client(client_socket, client_address):
    # Discard initial data (e.g., Telnet negotiation strings)
    initial_data = client_socket.recv(1024)
    print(initial_data)
    # Welcome message
    client_socket.send(b"Welcome to the Fake Telnet Server!\n")
    client_socket.send(b"Enter your username: ")
    username = client_socket.recv(1024).rstrip().decode()  # Convert bytes to string
    client_socket.send(b"Enter your password: ")
    password = client_socket.recv(1024).rstrip().decode()  # Convert bytes to string
    
    # Check credentials
    if username == "admin" and password == "password":
        client_socket.send(b"Login successful!\n")
        client_socket.send(b"Available commands: info, list, quit\n")

        while True:
            client_socket.send(b"\nEnter command: ")
            command = client_socket.recv(1024).rstrip().decode().lower()  # Convert bytes to string
            
            # Log command
            logger(client_address[0], client_address[1], command)
            
            # Execute command
            if command == "info":
                client_socket.send(b"This is a fake Telnet server.\n")
            elif command == "list":
                client_socket.send(b"List of items:\n- Item 1\n- Item 2\n- Item 3\n")
            elif command == "quit":
                client_socket.send(b"Goodbye!\n")
                break
            else:
                client_socket.send(b"Invalid command. Please try again.\n")
    else:
        client_socket.send(b"Login failed. Incorrect username or password.\n")

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
            
            handle_client(client_socket, client_address)
    except KeyboardInterrupt:
        print("\n[*] Exiting...")
        server_socket.close()
        sys.exit()

if __name__ == "__main__":
    main()

