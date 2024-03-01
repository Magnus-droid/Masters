#!/bin/bash

# Define a function to handle incoming connections
handle_connection() {
    while true; do
        # Accept incoming connections on port 23 and execute the fake console script
        nc -l -p 23 -q 1 < /home/ubuntu/Masters/fake_shell/fake_console.sh
    done
}

# Call the function to handle connections
handle_connection

