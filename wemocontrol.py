from w3mo import w3mo
import time

def latte(state, device):

    devices = w3mo.discover(return_type=list)

#define device as the control class instantiation at index 0 of devices
    device1 = devices[0]['obj']
    device2 = devices[1]['obj']
    device3 = devices[2]['obj']
#device name and state are set at instantiation and updated throughout use
    print("Device Name = {}".format(device2.name))
    print("Device State = {}".format(device2.state))
    print("Device Name = {}".format(device1.name))
    print("Device State = {}".format(device1.state))
    print("Device Name = {}".format(device3.name))
    print("Device State = {}".format(device3.state))
    
    if device1.name == device:
        print('good job')
        if state == 0:
            device1.set_state(0)
        elif state == 1:
            device1.set_state(1)
    elif device2.name == device:
        print('good job')
        if state == 0:
            device2.set_state(0)
        elif state == 1:
            device2.set_state(1)
    elif device3.name == device:
        print('good job')
        if state == 0:
            device3.set_state(0)
        elif state == 1:
            device3.set_state(1)
   
#turn on



#time.sleep(.25)
#turn off
#device.set_state(0)

