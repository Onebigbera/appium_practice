# -*-coding:utf-8 -*-
# File :LoginView.py
# Author:George
# Date : 2019/10/24
# motto: Someone always give up while someone always try!
"""
    LoginView    Business logic encapsulation
"""
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from common_fun import Common
from logging_driver_ import logging
from get_config import get_driver_


class LoginAction(Common):
    username_loc = (By.CLASS_NAME, 'android.widget.EditText')
    password_loc = (By.ID, 'com.tal.kaoyan:id/login_password_edittext')
    click_loc = (By.ID, 'com.tal.kaoyan:id/login_login_btn')

    def login(self, username, password):
        self.check_cancelBtn()
        self.check_skipBtn()
        sleep(1)
        try:
            username_input = self.find_element(*self.username_loc)
        except NoSuchElementException:
            logging.info("=====account input does not exist in page =====")
        else:
            username_input.send_keys(username)
            logging.info("=====input username====")

        try:
            password_input = self.find_element(*self.password_loc)
        except NoSuchElementException:
            logging.info("=====password input does not exist in page =====")
        else:
            password_input.send_keys(password)
            logging.info("=====input password====")

        try:
            login_btn = self.find_element(*self.click_loc)
        except NoSuchElementException:
            logging.info("=====login btn does not exist in page =====")
        else:
            login_btn.click()
            logging.info("=====click to login====")


def main():
    """test class LoginView"""
    driver = get_driver_()
    login_action= LoginAction(driver)
    account = ('george9527', 'george9527')
    login_action.login(account[0], account[1])
    driver.close_app()


if __name__ == "__main__":
    main()






