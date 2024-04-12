from datetime import datetime

# Get current timestamp

ip_commands = {}

attacker_ip = "some IP"



with open("/home/ubuntu/Masters/logs/45.76.145.129.log", 'r') as file:
    full_line = file.readlines()

ip_commands[attacker_ip] = full_line

for line in full_line:
    print(line)
    split_line = line.strip().split(']')
    if len(split_line) > 1:
     command = split_line[1]
    print(command)

with open("/home/ubuntu/Masters/imports/test", 'a') as combined:
     for ip, commands in ip_commands.items():
         combined.write(f"[{ip}]\n\n")
         combined.writelines(commands)
         combined.write("----------------------------------------\n\n")



