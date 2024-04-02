

color_strings = {"help-vehicle":
"""\033[0m\033[1m\033[31mHelp :
\033[0m\033[36mcmd \033[0m\033[33m[option1|option2]{string}(number) \033[0m

\033[1m\033[31mBuiltins :
\033[0m\033[36mcversion \033[0m\033[33m \033[0m          Console version
\033[36mhelp \033[0m\033[33m \033[0m              Display help
\033[36mscreen \033[0m\033[33m[(X)] \033[0m       Change to screen X. If no argument, display screen list
\033[36mcolor \033[0m\033[33m[0|1] \033[0m        Enable/Disable color output
\033[36mlang \033[0m\033[33m[{str}] \033[0m       Set the console language
\033[36mreboot \033[0m\033[33m[(waitTime)] \033[0mReboot
\033[36mcompletion \033[0m\033[33m \033[0m        Activate advanced completion
\033[36mexit \033[0m\033[33m \033[0m              Quit

\033[1m\033[31mBasics :
\033[0m\033[36m1wire \033[0m\033[33m \033[0m             Display 1wire information
\033[36miostate \033[0m\033[33m \033[0m           Display input/output state
\033[36mmodem \033[0m\033[33m \033[0m             Display modem state
\033[36mgpspos \033[0m\033[33m \033[0m            Retrieve last GPS position
\033[36mlist \033[0m\033[33m[all|{module}][dl] \033[0mList available modules.
                    [all] List all available modules parameters.
                    [module] List available module parameters.
                    [dl] Download result.
\033[36mg \033[0m\033[33m{module} {parameter} [(index)] \033[0mGet module parameter value
\033[36ms \033[0m\033[33m{module} {parameter} [(index)] {value} \033[0mSet module parameter value
\033[36mlistdb \033[0m\033[33m \033[0m            List available DB parameters
\033[36mgdb \033[0m\033[33m{name} \033[0m         Get a DB parameter
\033[36msdb \033[0m\033[33m{name} {value} \033[0m Set a DB parameter
\033[36mlog \033[0m\033[33m[print|debug|warn|error|{str}] \033[0mDisplay last log
\033[36mlogdump \033[0m\033[33m[print|debug|warn|error|{str}] \033[0mDisplay all logs
\033[36mconfigure \033[0m\033[33m \033[0m         Upload a new conf file

""",

"screen":
"""\033[36mscreen 0\033[0m    Basics
\033[36mscreen 1\033[0m    Advanced
\033[36mscreen 2\033[0m    Commands
""",

"screen 1":
"""\033[1m\033[31mAdvanced :
\033[0m\033[36mip \033[0m\033[33m[{str}] \033[0m         Display all ip addresses. If str, display only str address.
\033[36mstats \033[0m\033[33m \033[0m             Display stats.
\033[36mllog \033[0m\033[33m[soft|gps|update|kstart|mAT|mPPP] \033[0mDisplay last logs of:
                    software, gps, kernel start, modem AT, or modem PPP
\033[36mskey \033[0m\033[33m[update|delete] \033[0mUpdate|Delete server key
\033[36mukey \033[0m\033[33m[update|delete] \033[0mUpdate|Delete user key
\033[36mlogs \033[0m\033[33m[get|delete][all|{filename}|crashes] \033[0mRetrieve or Delete logs of software
\033[36mstopsoft \033[0m\033[33m \033[0m          Stop the software
\033[36musercpn \033[0m\033[33m[list|start|stop|remove][all|{cpnName}] \033[0mList user components
\033[36mgprsupdate \033[0m\033[33m[start|stop] \033[0mEnable / Disable GRPS update
\033[36mgeomap \033[0m\033[33m[update|delete] \033[0mUpdate / Delete a geofencing map
\033[36mupdate \033[0m\033[33m \033[0m            Upload an update package
\033[36mrestore \033[0m\033[33m[all|write|pdm|db|user] \033[0mRestore parameters of write, db or pbm
\033[36mrestoreFull \033[m\033[33m \033[0m       Restore device to the initial configuration state
\033[36mversion \033[m\033[33m \033[0m           Display software/hardware version
\033[36mremote \033[m\033[33m[{ip}] \033[0m      Console on remote device
\033[36mcpu \033[m\033[33m[{cpnName}] \033[0m    Get CPU usage for group

""",

"screen 2":
"""\033[1m\033[31mCommands :
\033[0m\033[36mclist \033[0m\033[33m \033[0m             List available commands
\033[36mchelp \033[0m\033[33m{cmdName} \033[0m    Display command help
\033[36mcxelp \033[0m\033[33m{cmdRName} \033[0m   Find and display command help
\033[36mcrun \033[0m\033[33m{cmdName}[{cmdArgs}] \033[0mRun the command
\033[36mcexe \033[0m\033[33m{cmdRName}[{cmdArgs}] \033[0mFind and run the command (example: cexe .*_EnergyReferee.cmd...)
""",

"welcome":
"""\033[1m\033[35mWelcome on console


""",

"help-cloud":
"""\033[0m\033[1m\033[31mWelcome on console\033[0m

\033[0m\033[1m\033[31mHelp :\033[0m
\033[0m\033[36mcmd \033[0m\033[33m[option1|option2]{string}(number) \033[0m

\033[1m\033[31mBuiltins :\033[0m
\033[0m\033[36mcversion \033[0m\033[33m\033[0m          Console version
\033[36mhelp \033[0m\033[33m\033[0m               Display help
\033[36mscreen \033[0m\033[33m[(X)] \033[0m       Change to screen X. If no argument, display screen list
\033[36mcolor \033[0m\033[33m[0|1] \033[0m        Enable/Disable color output
\033[36mlang \033[0m\033[33m[{str}] \033[0m       Set the console language
\033[36mreboot \033[0m\033[33m[(waitTime)] \033[0mReboot
\033[36mcompletion \033[0m\033[33m\033[0m         Activate advanced completion
\033[36mexit \033[0m\033[33m\033[0m               Quit

\033[1m\033[31mVehicle Management :\033[0m
\033[36mstatus \033[0m\033[33m\033[0m             Display vehicle status and diagnostics
\033[36mgpspos \033[0m\033[33m\033[0m             Retrieve last GPS position of vehicles
\033[36mtelemetry \033[0m\033[33m\033[0m          View telemetry data from vehicle sensors
\033[36mdiagnostics \033[0m\033[33m\033[0m        Run diagnostic tests on vehicle systems
\033[36mfirmware \033[0m\033[33m\033[0m           Update vehicle firmware

\033[1m\033[31mCloud Services :\033[0m
\033[36minstances \033[0m\033[33m\033[0m          Manage cloud instances and virtual machines
\033[36mstorage \033[0m\033[33m\033[0m            Manage cloud storage resources
\033[36mnetworking \033[0m\033[33m\033[0m         Configure networking settings for cloud deployments
\033[36msecurity \033[0m\033[33m\033[0m           Monitor and manage security configurations

"""}
