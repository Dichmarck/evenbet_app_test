import time
from typing import Tuple, List, Any, Optional, Union
from evenbet_app_test.locators.locators import *
from evenbet_app_test.pages.BasePage import BasePage
from evenbet_app_test.constants import *
import pyautogui
import pytest


class LoginPage(BasePage):

    def should_appear_login_window(self, timeout=10, confidence=0.8):
        login_window = self.does_element_appear(LoginPageLocators.LOGIN_WINDOW, confidence=confidence, timeout=timeout)
        assert login_window, "Login window didn't appear"
        return login_window

    def should_be_sign_up_button(self, confidence=0.8):
        sign_up_button = self.is_element_present(LoginPageLocators.SIGNUP_BUTTON, confidence=confidence)
        assert sign_up_button, "No Sign-Up button at Login page"
        return sign_up_button

    def click_sign_up_button(self, confidence=0.8):
        sign_up_button = self.should_be_sign_up_button(confidence=confidence)
        pyautogui.moveTo(sign_up_button[0], sign_up_button[1], duration=FAST)
        pyautogui.click()

    def should_appear_sign_up_window(self, timeout=10, confidence=0.8):
        signup_win = self.does_element_appear(LoginPageLocators.SIGNUP_WINDOW, confidence=confidence, timeout=timeout)
        assert signup_win, "Sign-Up window didn't appear after clicking Sign-Up button on Login Page"
        return signup_win

    def should_be_nick_field(self, confidence=0.8):
        nick_field = self.is_element_present(LoginPageLocators.NICK_FIELD, confidence=confidence)
        assert nick_field, "No Nick field on Sign-Up page"
        return nick_field

    def find_nick_field_click_it_and_type_nick(self, nick, confidence=0.8):
        nick_field = self.should_be_nick_field(confidence=confidence)
        pyautogui.moveTo(nick_field[0], nick_field[1], duration=FAST)
        pyautogui.click()
        pyautogui.typewrite(nick, interval=0.01)

    def should_be_email_field(self, confidence=0.8):
        email_field = self.is_element_present(LoginPageLocators.EMAIL_FIELD, confidence=confidence)
        assert email_field, "No Email field on Sign-Up page"
        return email_field

    def find_email_field_click_it_and_type_email(self, email, confidence=0.8):
        email_field = self.should_be_email_field(confidence=confidence)
        pyautogui.moveTo(email_field[0], email_field[1], duration=FAST)
        pyautogui.click()
        pyautogui.typewrite(email, interval=0.01)
        
    def should_be_password1_field(self, confidence=0.8):
        password1_field = self.is_element_present(LoginPageLocators.PASSWORD_FIELD, confidence=confidence)
        assert password1_field, "No Password-1 field on Sign-Up page"
        return password1_field

    def find_password1_field_click_it_and_type_password(self, password1, confidence=0.8):
        password1_field = self.should_be_password1_field(confidence=confidence)
        pyautogui.moveTo(password1_field[0], password1_field[1], duration=FAST)
        pyautogui.click()
        pyautogui.typewrite(password1, interval=0.01)

    def should_be_password2_field(self, confidence=0.8):
        password2_field = self.is_element_present(LoginPageLocators.PASSWORD_FIELD, confidence=confidence)
        assert password2_field, "No Password-2 field on Sign-Up page"
        return password2_field

    def find_password2_field_click_it_and_type_password(self, password2, confidence=0.8):
        password2_field = self.should_be_password2_field(confidence=confidence)
        pyautogui.moveTo(password2_field[0], password2_field[1], duration=FAST)
        pyautogui.click()
        pyautogui.typewrite(password2, interval=0.01)

    def should_be_send_button_field(self, confidence=0.8):
        send_button_field = self.is_element_present(LoginPageLocators.SEND_BUTTON, confidence=confidence)
        assert send_button_field, "No Send button on Sign-Up page"
        return send_button_field

    def click_send_button(self, confidence=0.8):
        send_button = self.should_be_send_button_field(confidence=confidence)
        pyautogui.moveTo(send_button[0], send_button[1], duration=FAST)
        pyautogui.click()

    def should_appear_user_test_avatar(self, timeout=10, confidence=0.8):
        avatar = self.does_element_appear(LoginPageLocators.USER_TEST_AVATAR, confidence=confidence, timeout=timeout)
        assert avatar, "User Avatar didn't appear after registration"
        return avatar
