import inputs
import threading
import os
import time
print("WE OUT")



if __name__ == "__main__":
    while True:
        events = inputs.devices.keyboards[0].read()
        
        keys_down = any(event.state == inputs.KEY_STATE_DOWN for event in events)
        if keys_down:
            print("SHUTDOWN")
        else:
            print("FAIL")