import bluetooth
import pyautogui
import time

# Define the Bluetooth device address
device_address = 'XX:XX:XX:XX:XX:XX'  # Replace with the Bluetooth device address

# Connect to the Bluetooth device
socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
socket.connect((device_address, 1))

# Define the path to the Ducky Script (bin) file
ducky_script_file = 'script.bin'  # Replace with the path to your Ducky Script file

# Read the contents of the Ducky Script file
with open(ducky_script_file, 'rb') as file:
    ducky_script = file.read()

# Send the Ducky Script commands
socket.send(ducky_script)

# Wait for the commands to be executed
time.sleep(1)  # Adjust the delay if needed

# Close the Bluetooth connection
socket.close()

# Optional: Simulate Enter key press to finish execution
pyautogui.press('enter')