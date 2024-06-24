# Examining vehicle honeypot attack data under the scope of existing frameworks

## Structure
This repository contains the following folders:
1) `command data` - fake data that the honeypot should send to its clients when prompted
2) `images` - notable images (more relevant during the development process)
3) `imports` - Anything the scripts need to function properly
4) `logs` - data collected by the honeypot
5) `malware col` - contains the executables attempted by attackers
6) `scrips` - scripts for running the server automatically on bootup and attaching an additional VNIC to the instance

## Oracle Cloud Setup:
The virtual machine that the honeypot in this project is run on is rented from the [Oracle Cloud Infrastructure](https://www.oracle.com/cloud/).
Once an account has been created, the user can rent up to two AMD Compute VMs for free. The steps for setting up these VMs are listed below:
1) Navigate to `Instances` and create an instance with the desired OS, memory size and processor.
2) This involves creating a subnet, VCN and VNIC. Additionally, creating a network security group with ingress and engress rules for the instance is advised here.
3) Log into the instance via SSH.
4) If more than one IP address for the honeypot is desired, this means that an additional VNIC has to be created and attached to the instance. This step is best explained by [this video](https://www.youtube.com/watch?v=amYLnXEDs9w&ab_channel=OracleLearning).
5) The script in question can be found in the [scripts folder](scripts/).
This concludes setting up an Oracle Cloud instance.

## Honeypot Commands
1) Start server on OCI launch:
	`crontab -e` -> `@reboot /home/ubuntu/Masters/run_vehicle_server.sh`
2) Open for telnet traffic on the honeypot (in case there are firewall problems)
   	`-A INPUT -p tcp -m state --state NEW -m tcp --dport 23 -j ACCEPT` in `/etc/iptables/rules.v4`

