import time
from typing import Optional, Tuple
import pyautogui
import pytest
from .pages.BasePage import BasePage
from evenbet_app_test.constants import *
from .locators.locators import *

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


@pytest.fixture
def app():
    fixture_basepage = BasePage(pyautogui.size())

    taskbar_app_icon = fixture_basepage.does_element_appear(BasePageLocators.TASKBAR_APP_ICON)
    desktop_app_icon = fixture_basepage.does_element_appear(BasePageLocators.APP_ICON)
    if taskbar_app_icon:
        pyautogui.click(taskbar_app_icon[0], taskbar_app_icon[1], duration=DEFAULT)
        #print("taskbar_app_icon")
    elif desktop_app_icon:
        pyautogui.click(desktop_app_icon[0], desktop_app_icon[1], duration=DEFAULT)
        #print("desktop_app_icon")

    poker_logo = fixture_basepage.does_element_appear(BasePageLocators.POKER_LOGO, timeout=30, confidence=0.9)
    if poker_logo:
        pyautogui.moveTo(poker_logo[0], poker_logo[1], duration=DEFAULT)
        #print("poker_logo")

    evenbet_poker_title = fixture_basepage.is_element_present(BasePageLocators.EVENBET_POKER_LEFT_TOP)
    app_left = evenbet_poker_title[0]
    app_top = evenbet_poker_title[1]
    app_width = fixture_basepage.size[0] - app_left - 1
    app_height = fixture_basepage.size[1] - app_left - 1
    #print(app_left, app_top, app_width, app_height)

    close_white_cross = fixture_basepage.does_element_appear(BasePageLocators.CLOSE_DIALOG_WHITE_CROSS,
                        left=app_left, top=app_top, width=app_width, height=app_height)
    if close_white_cross:
        #print("close_white_cross")
        pyautogui.click(close_white_cross[0], close_white_cross[1], duration=SLOW)
        time.sleep(2)

    fullscreen_button = fixture_basepage.does_element_appear(BasePageLocators.FULLSCREEN_BUTTON)
    if fullscreen_button:
        #print("fullscreen_button")
        pyautogui.click(fullscreen_button[0], fullscreen_button[1], duration=DEFAULT)

    yield

    close_white_cross = fixture_basepage.does_element_appear(BasePageLocators.CLOSE_DIALOG_WHITE_CROSS,
                                                        left=app_left, top=app_top, width=app_width, height=app_height)
    while close_white_cross:
        #print("close_white_cross")
        pyautogui.click(close_white_cross[0], close_white_cross[1], duration=SLOW)
        close_white_cross = fixture_basepage.does_element_appear(BasePageLocators.CLOSE_DIALOG_WHITE_CROSS, timeout=2)

    close_app_button = fixture_basepage.is_element_present(BasePageLocators.CLOSE_APP_RIGHT_TOP_BUTTON, confidence=0.8)
    if close_app_button:
        #print("close_app_button")
        pyautogui.click(close_app_button[0], close_app_button[1], duration=DEFAULT)
        time.sleep(2)

    green_yes_button = fixture_basepage.does_element_appear(BasePageLocators.GREEN_YES_BUTTON)
    if green_yes_button:
        #print("green_yes_button")
        pyautogui.click(green_yes_button[0], green_yes_button[1], duration=DEFAULT)


#app()


