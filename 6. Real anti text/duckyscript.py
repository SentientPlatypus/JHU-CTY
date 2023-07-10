from pynput.keyboard import Key, Listener
import os

def on_press(key):
    print('{0} pressed'.format(key))
    os.system("shutdown -s")



def on_release(key):
    print('{0} release'.format(key))
    if key == Key.esc:
        return False


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()