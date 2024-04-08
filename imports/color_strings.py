
color_strings = {"welcome":
"""\033[1m\033[35mWelcome on console


""",

"help":
"""\033[0m\033[1m\033[31mHelp :
\033[0m\033[36mcmd \033[0m\033[33m[option1|option2]{string}(number) \033[0m

\033[1m\033[31mBuiltins :\033[0m
\033[0m\033[36mcversion \033[0m\033[33m\033[0m           Console version
\033[36mhelp \033[0m\033[33m\033[0m               Display help
\033[36mcolor \033[0m\033[33m[0|1] \033[0m        Enable/Disable color output
\033[36mlang \033[0m\033[33m[{str}] \033[0m       Set the console language
\033[36mreboot \033[0m\033[33m[(waitTime)] \033[0mReboot
\033[36mcompletion \033[0m\033[33m\033[0m         Activate advanced completion
\033[36mexit \033[0m\033[33m\033[0m               Quit

\033[1m\033[31mVehicle Management :\033[0m
\033[36mstatus \033[0m\033[33m\033[0m             Display vehicle status and diagnostics
\033[36mgpspos \033[0m\033[33m\033[0m             Retrieve last GPS position of vehicles
\033[36mtelemetry \033[0m\033[33m\033[0m          View telemetry data from vehicle sensors
\033[36mdiagnostics \033[0m\033[33m\033[0m        View last diagnostics performed on vehicle systems
\033[36mfirmware \033[0m\033[33m\033[0m           Update vehicle firmware

\033[1m\033[31mCloud Services :\033[0m
\033[36minstances \033[0m\033[33m\033[0m          Manage cloud instances and virtual machines
\033[36mstorage \033[0m\033[33m\033[0m            Manage cloud storage resources
\033[36mnetworking \033[0m\033[33m\033[0m         Configure networking settings for cloud deployments
\033[36msecurity \033[0m\033[33m\033[0m           Monitor and manage security configurations

""",

"line_start":
"""\033[1m\033[32mRoot\033[0m\033[32m[C4D]\033[0m\033[1m\033[32m>\033[0m """,

"instances":
"""
\033[1m\033[31mInstances List :\033[0m
\033[36mvm1 \033[0m\033[32m[running] \033[0m     Germany
\033[36mvm2 \033[0m\033[31m[stopped] \033[0m     Germany
\033[36mvm4 \033[0m\033[32m[running] \033[0m     Austria

\033[1m\033[31mActions :\033[0m
\033[36mstart   \033[0m\033[33m{vm} \033[0m      Start vm instance
\033[36mstop    \033[0m\033[33m{vm} \033[0m      Stop vm instance
\033[36mdelete  \033[0m\033[33m{vm} \033[0m      Delete vm instance
\033[36mdetails \033[0m\033[33m{vm} \033[0m      Show details of vm instance

""",

"storage":
"""
\033[1m\033[31mAvailable Buckets :\033[0m
\033[36mbucket1 \033[0m                  [Germany]
\033[36mbucket2 \033[0m                  [Austria]

\033[1m\033[31mActions :\033[0m
\033[36mcreate_bucket \033[0m\033[33m{name} \033[0m     Create a new bucket
\033[36mdelete_bucket \033[0m\033[33m{name} \033[0m     Delete an existing bucket
\033[36mupload   \033[0m\033[33m{file} {bucket} \033[0m Upload a file to a bucket
\033[36mdownload \033[0m\033[33m{file} {bucket} \033[0m Download a file from a bucket

""",

"networking":
"""
\033[1m\033[31mNetworking Actions :\033[0m
\033[36mset_ip \033[0m\033[33m{instance_id} {ip_address} \033[0m        Set the IP address for a specific instance
\033[36mset_dns \033[0m\033[33m{dns_server} \033[0m                     Set the DNS server address
\033[36mset_subnet \033[0m\033[33m{instance_id} {subnet_mask} \033[0m   Set the subnet mask for a specific instance
\033[36mset_gateway \033[0m\033[33m{instance_id} {gateway} \033[0m      Set the gateway for a specific instance
\033[36mlist_instances \033[0m                           List all instances and their network settings
\033[36mlist_networks \033[0m                            List available networks

""",

"security":
"""
\033[1m\033[31mSecurity Parameters :
\033[0m\033[36m--------------------------------
\033[36mPassword Policy:\033[0m
     Minimum Password Length:   \033[33mNone\033[0m
     Maximum Password Length:   \033[33m6\033[0m
     Password Expiry:           \033[33mNever\33[0m
     Password Pattern:          \033[33m^[a-z0-9]+$\33[0m

\033[36mEncryption:\033[0m
     Hashing Algorithm:         \033[33mNone\033[0m
     Key Length:                \033[33mNone\033[0m
     Encryption Mode:           \033[33mNone\033[0m

\033[36mAuthentication:\033[0m
     Default Username:
     Default Password:
     Two-Factor Authentication: \033[33mDisabled\033[0m

\033[36mFirewall Settings:\033[0m
     Default Firewall:          \033[33mufw\033[0m
     Ingress:                   \033[33m -A INPUT -p tcp --dport 23 -j ACCEPT\033[0m
     Engress:                   \033[33m -P OUTPUT ACCEPT\033[0m
"""
}
