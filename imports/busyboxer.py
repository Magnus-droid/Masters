def busyboxer(command):
    components = command.split(' ')
    if len(components) > 1:
        bb_command = components[1:]
        bb_response = f"{bb_command}: applet not found\n"
        print(bb_response)
    else:
        with open('/home/ubuntu/Masters/command_data/fake_busy_box', 'rb') as f:
            f_content = f.read()
        print(f_content)

busyboxer('/bin/busybox ')
