# Low-interaction honeypot for telematic units in vehicles (Master's thesis)

## So far:
1) Oracle cloud VPS running on 130.61.249.221
2) Git connection set up
3) Fake telent socket on port 23 reachable from all IPs
4) Command logging based on IP
5) Different IPs:
	- set DNS server: `nameserver 8.8.8.8` in /etc/resolv.conf
        - `sudo su`
	- `./secondary_vnic_all_configure.sh -c`   


## TODOs 
1) Allow multiple connection
2) Imporve console commands
3) Split project into more filessuch as:
   - fake_console.py (design of what the console should look like)
   - request_handler.py (handles multiple requests, makes instances for each IP with memory maybe?)
   - server.py (sets up a proper telnet sever with a different IP than the VPS)
   - device_info.py (adds fake information in order to disguse the VPS) 
