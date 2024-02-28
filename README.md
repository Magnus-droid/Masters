# Low-interaction honeypot for telematic units in vehicles (Master's thesis)

## So far:
1) Oracle cloud VPS running on 130.61.249.221
2) Git connection set up
3) Fake telent socket on port 23 reachable from all IPs
4) Command logging based on IP
5) Different IPs:
	- set DNS server: `nameserver 8.8.8.8` in /etc/resolv.conf
        - `sudo su`
	- ./secondary_vnic_all_configure.sh -c   


## TODOs
### 1) Change IP address so that it's not an obvious Oracle VPS
   - add an IP to the OS with the command `sudo ip addr add <ip_address>/<prefix length> dev ens3 label ens3` (prefix length seems to often just be 24) (has to be done after every reboot unless I make it perma)
   - delete it with `sudo ip addr del <ip_address>/<prfix length> dev ens3`
   - Right now this works if the same subnet with the same security rules is used -> this means that I cannot seperate which IP to open port 23 on and which not
   - Fix: 1) Need a routing table for my Virtual Cloud Network
          2) Need a Virtual Cloud Network for Subnet
          3) Need a Subnet for Virtual Cloud Network Card (bridge between instance and VCN)
   - All in all this allows me to add an additional reserved public IP address to my instance with different security rules. 
3) Allow multiple connection
4) Imporve console commands
5) Split project into more filessuch as:
   - fake_console.py (design of what the console should look like)
   - request_handler.py (handles multiple requests, makes instances for each IP with memory maybe?)
   - server.py (sets up a proper telnet sever with a different IP than the VPS)
   - device_info.py (adds fake information in order to disguse the VPS) 
