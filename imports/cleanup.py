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

    # Write updated command counts to the file
    with open(command_summary_file, 'w') as command_summary:
        for command, count in existing_command_counts.items():
            command_summary.write(f"{command}: {count}\n")

def generate_summary(logs_dir, ip_summary_file, command_summary_file):
    # Dictionary to store counts of commands attempted
    command_counts = {}

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
                commands = file.readlines()

            # Update count for each command
            for command in commands:
                command = command.strip()
                command_counts[command] = command_counts.get(command, 0) + 1
            
            # Remove the log file after processing
            os.chmod(filepath, 0o777)
            os.remove(filepath)

    # Write unique attacker IPs to file
    with open(ip_summary_file, 'w') as ip_summary:
        for ip in attacker_ips:
            ip_summary.write(ip + '\n')

    # Update command summary file with new counts
    update_command_counts(command_summary_file, command_counts)

    print("Summary generation complete.")


# Directory where .log files are stored
logs_directory = "/home/ubuntu/Masters/logs"

# File to store summary of unique attacker IPs
ip_summary_file = "/home/ubuntu/Masters/logs/ip_summary_file.txt"

# File to store summary of command attempts
command_summary_file = "/home/ubuntu/Masters/logs/command_summary_file.txt"

# Generate the summary
generate_summary(logs_directory, ip_summary_file, command_summary_file)

