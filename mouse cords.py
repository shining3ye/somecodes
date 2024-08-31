import pyautogui
import time

try:
    while True:
        # Get the current position of the cursor
        cursor_position = pyautogui.position()
        
        # Print the position
        print(f"Cursor Position: {cursor_position}")
        
        # Sleep for a short duration to avoid spamming output too quickly
        time.sleep(0.1)  # Adjust the time as needed (0.1 = 100 ms)
        
except KeyboardInterrupt:
    print("\nProgram stopped.")