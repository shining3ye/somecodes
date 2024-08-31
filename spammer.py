import time
import pyautogui

# The Thong You want to spam/nuke
message = "This is a FATMAN!"
# Time delay between each message
delay = 0.25  # (0.025-1.5) seconds

# Short delay before the script starts, so you can switch to the input field
print("Starting in 5 seconds...")
time.sleep(1)
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")

# here the msg loop starts
while True:
    pyautogui.typewrite(message)
    pyautogui.press("enter")
    time.sleep(delay)
