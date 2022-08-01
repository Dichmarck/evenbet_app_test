import time
from typing import Tuple, List, Any, Optional, Union
from evenbet_app_test.locators.locators import *
from evenbet_app_test.constants import *
import pyautogui
import pytest


class BasePage:
    def __init__(self, screen_size:  Tuple[int]):
        self.size = screen_size

    def does_element_appear(self, locator: str, confidence: float = 0.8, timeout: float = 5, left: int = 0,
                            top: int = 0, width: int = 0, height: int = 0) -> Optional[Tuple[int]]:
        if width == 0:
            width = self.size[0]
        if height == 0:
            height = self.size[1]

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

    def is_element_present(self, locator: str, confidence: float = 0.8, left: int = 0, top: int = 0, width: int = 0,
                            height: int = 0) -> Optional[Tuple[int]]:
        if width == 0:
            width = self.size[0]
        if height == 0:
            height = self.size[1]

        center_coords = pyautogui.locateCenterOnScreen(locator, confidence=confidence,
                                                       region=(left, top, width, height))
        return center_coords


