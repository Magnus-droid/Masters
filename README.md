# Low-interaction honeypot for telematic units in vehicles (Master's thesis)

## So far:
1) Oracle cloud VPS running on 130.61.249.221 (reachable via telnet only on 150.230.146.110)
2) Git connection set up
4) Fake telent socket on port 23 reachable from all IPs
5) Command logging based on IP
6) Different IPs:
        - `sudo su`
	- `./secondary_vnic_all_configure.sh -c`   
7) Able to handle multiple clients
8) Console view for help() function completed ![console](pics/telnet_console_view.png) 
9) Start server on OCI launch.:
	`crontab -e` -> `@reboot /home/ubuntu/Masters/run_vehicle_server.py`
10) added telnet connection after running script via `-A INPUT -p tcp -m state --state NEW -m tcp --dport 23 -j ACCEPT` after the similar ssh line in the file `/etc/iptables/rules.v4`

## TODOs 
2) Imporve console commands
3) Split project into more filessuch as:
   - fake_console.py (design of what the console should look like)
   - request_handler.py (handles multiple requests, makes instances for each IP with memory maybe?)
   - server.py (sets up a proper telnet sever with a different IP than the VPS)
   - device_info.py (adds fake information in order to disguse the VPS) 
4) proper error handeling so the server cannot be crashed, no matter the input
5) proper kill switch on CTRL+C, force threads to join and terminate them
