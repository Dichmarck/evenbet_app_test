import time

import pyautogui, sys

while True:
    position = pyautogui.position()
    print(f"X: {position[0]}, Y: {position[1]}")
    time.sleep(0.2)
    if position == (0, 0):
        break
