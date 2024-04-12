from datetime import datetime

def logger(ip_address, port, command):
    #log commands from IP addresses and port
    time_now = datetime.utcnow().isoformat(sep=' ', timespec='milliseconds')
    if command:
        with open(f"/home/ubuntu/Masters/logs/{ip_address}.log", "a") as log_file:
            log_file.write(f"[{time_now}] {command}\n")


