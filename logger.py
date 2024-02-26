def logger(ip_address, port, command):
    #log commands from IP addresses and ports
    with open("logs/"+str(ip_address)+".log", "a") as log_file:
        log_file.write(f"{ip_address}:{port}: {command}\n")


