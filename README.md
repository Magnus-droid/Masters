# Low-interaction honeypot for telematic units in vehicles (Master's thesis)

## So far:
1) Oracle cloud VPS running on 130.61.249.221
2) Fake telent socket on port 23 reachable from all IPs
3) Command logging based on IP


## TODOs
1) Change IP address so that it's not an obvious Oracle VPS
2) Allow multiple connection
3) Imporve console commands
4) Split project into more filessuch as:
   - fake_console.py (design of what the console should look like)
   - request_handler.py (handles multiple requests, makes instances for each IP with memory maybe?)
   - server.py (sets up a proper telnet sever with a different IP than the VPS)
   - device_info.py (adds fake information in order to disguse the VPS) 
