import time
from typing import Optional, Tuple
import pyautogui
import pytest
import os
from evenbet_app_test.constants import *

TASKBAR_APP_ICON = r"locators\windows\taskbar_app_icon.png"
APP_ICON = r"locators\windows\app_icon.png"
CLOSE_BUTTON = r"locators\windows\close_app_button.png"
YES_BUTTON = r"locators\base\yes_button.png"


def does_element_appear(locator: str, confidence: float = 0.8, timeout: float = 5, left: int = 0,
                        top: int = 0, width: int = 0, height: int = 0) -> Optional[Tuple[int]]:
    if width == 0:
        width = pyautogui.size()[0]
    if height == 0:
        height = pyautogui.size()[1]

    center_coords = None
    time_start = time.time()
    time_now = time.time()
    while time_now - time_start < timeout:
        center_coords = pyautogui.locateCenterOnScreen(locator, confidence=confidence,
                                                       region=(left, top, width, height))
        if center_coords is not None:
            break
        time_now = time.time()
    return center_coords


#@pytest.fixture
def app():
    taskbar_app_icon = does_element_appear(TASKBAR_APP_ICON)
    desktop_app_icon = does_element_appear(APP_ICON)
    if taskbar_app_icon:
        pyautogui.moveTo(taskbar_app_icon[0], taskbar_app_icon[1], duration=DEFAULT)
        pyautogui.click()
    elif desktop_app_icon:
        pyautogui.moveTo(desktop_app_icon[0], desktop_app_icon[1], duration=DEFAULT)
        pyautogui.click()

    #yield

    close_app_button = does_element_appear(CLOSE_BUTTON, timeout=20)
    if close_app_button:
        pyautogui.moveTo(close_app_button[0], close_app_button[1], duration=FAST)
        pyautogui.click()


app()


