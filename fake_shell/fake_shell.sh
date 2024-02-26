#!/bin/bash

# Display a fake login prompt
echo "login:"

# Read user input
read username

# Display a fake password prompt
echo "password:"

# Read user input (Note: This is insecure and for demonstration purposes only)
read password

# Print a fake welcome message
echo "Welcome, $username!"

# Set initial working directory
current_directory="/home/$username"

# Loop to simulate a command prompt
while true; do
    # Display a fake command prompt with the current directory
    echo -n "$username@$HOSTNAME:$current_directory$ "

    # Read user input
    read -a command_array

    # Extract the command and its arguments from the array
    command="${command_array[0]}"
    args="${command_array[@]:1}"

    # Execute fake commands
    case "$command" in
        "ls")
            ls_command="ls $args"
            eval "$ls_command"
            ;;
        "ls -a")
            ls_command="ls -a $args"
            eval "$ls_command"
            ;;
        "cd")
            # Change directory
    	    new_directory=$(cd "$args" && pwd)
    	    allowed_directories=("/home/$username" "/var/www/html")  # Add more allowed directories as needed

    	    # Check if the new directory is within the list of allowed directories
            if [[ " ${allowed_directories[@]} " =~ " $new_directory " ]]; then
                current_directory="$new_directory"
            else
                echo "bash: cd: $args: No such directory"
            fi
            ;;
        "pwd")
            echo "$current_directory"
            ;;
        "exit")
            break
            ;;
        *)
            echo "bash: $command: command not found"
            ;;
    esac
done

