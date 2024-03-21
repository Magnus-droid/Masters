#!/bin/bash

#!/bin/bash

# Start with switching to root user
sudo su << EOF

# Commands to execute as root user
#echo "Running commands as root user..."

# Run a script in the root environment
./secondary_vnic_all_configure.sh -c

#echo "Finished running script"

exit

EOF

#echo "Finished exiting root environment"

# Execute another script with sudo privileges
sudo /home/ubuntu/Masters/telnet_server.py

#echo "Finished running telnet_server"


