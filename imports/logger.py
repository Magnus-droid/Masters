import requests
from time import sleep

def logger(ip_address, port, command):
    #log commands from IP addresses and port
    if command:
        with open(f"logs/{ip_address}.log", "a") as log_file:
            log_file.write(f"{command}\n")
    else:
        with open(f"logs/no_command_IPs.log", "a") as f:
            f.write(f"{ip_address}\n")
            sleep(1)
