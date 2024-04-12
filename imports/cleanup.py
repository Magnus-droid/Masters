import os

def update_command_counts(command_summary_file, new_command_counts):
    # Dictionary to store existing command counts
    existing_command_counts = {}

    # Read existing command counts from the file, if it exists
    if os.path.exists(command_summary_file):
        with open(command_summary_file, 'r') as command_summary:
            for line in command_summary:
                command, count = line.strip().split(': ')
                existing_command_counts[command] = int(count)

    # Update existing command counts with new counts
    for command, count in new_command_counts.items():
        existing_command_counts[command] = existing_command_counts.get(command, 0) + count

    # Overwrite updated command counts to the file
    with open(command_summary_file, 'w') as command_summary:
        for command, count in existing_command_counts.items():
            command_summary.write(f"{command}: {count}\n")

def generate_summary(logs_dir, ip_summary_file, command_summary_file, combined_file):
    # Dictionary to store counts of commands attempted
    command_counts = {}

    ip_commands = {}

    # Set to store unique attacker IPs
    attacker_ips = set()

    # Loop through all .log files in the directory
    for filename in os.listdir(logs_dir):
        if filename.endswith(".log"):
            filepath = os.path.join(logs_dir, filename)
            attacker_ip = filename[:-4]  # Extract attacker's IP from filename
            attacker_ips.add(attacker_ip)

            # Read commands from the log file
            with open(filepath, 'r') as file:
                timestamped_commands = file.readlines()

            ip_commands[attacker_ip] = timestamped_commands

            # Update count for each command
            for line in timestamped_commands:
                split_line = line.strip().split(']')
                if len(split_line) > 1:
                    command = split_line[1].strip()
                else:
                    command = line.strip() 
                command_counts[command] = command_counts.get(command, 0) + 1
            
            # Remove the log file after processing
            os.chmod(filepath, 0o777)
            os.remove(filepath)

    # Append unique attacker IPs to file
    with open(ip_summary_file, 'a') as ip_summary:
        for ip in attacker_ips:
            ip_summary.write(ip + '\n')
    
    with open(combined_file, 'a') as combined:
        for ip, commands in ip_commands.items():
            combined.write(f"[{ip}]\n\n")
            combined.writelines(commands)
            combined.write("---------------------------------------------\n\n")
    # Update command summary file with new counts
    update_command_counts(command_summary_file, command_counts)

    print("Summary generation complete.")


# Directory where .log files are stored
logs_directory = "/home/ubuntu/Masters/logs"

# File to store summary of unique attacker IPs
ip_summary_file = "/home/ubuntu/Masters/logs/ip_summary_file_console.txt"

# File to store summary of command attempts
command_summary_file = "/home/ubuntu/Masters/logs/command_summary_file_console.txt"

combined_file = "/home/ubuntu/Masters/logs/combined_file_console.txt"

# Generate the summary
generate_summary(logs_directory, ip_summary_file, command_summary_file, combined_file)

