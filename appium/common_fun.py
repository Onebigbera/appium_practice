# -*-coding:utf-8 -*-
# File :common_fun.py
# Author:George
# Date : 2019/10/24
# motto: Someone always give up while someone always try!
"""
    Common class which inherit BaseView  use logging model to record it  basic action
"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from logging_driver_ import logging
# from yaml_handler import logging
from pageObject.logic_business.baseView import BaseView
from get_config import get_driver_


class Common(BaseView):
    """
    cancel_btn and skip btn
    """
    # element locator
    cancel_loc = (By.ID, 'android:id/button2')
    skip_loc = (By.ID, 'com.tal.kaoyan:id/tv_skip')

    def check_cancelBtn(self):
        """
        if there is a update button cancel it then
        :return:
        """
        try:
            cancel_btn = self.find_element(*self.cancel_loc)
        except NoSuchElementException:
            logging.info("=====cancel button does not exist in page =====")
        else:
            cancel_btn.click()
            logging.info("=====Click Cancel btn====")

    def check_skipBtn(self):
        """
        to skip advertising
        :return:
        """
        try:
            skip_btn = self.find_element(*self.skip_loc)
        except NoSuchElementException:
            logging.info("=====skip button does not exist in page =====")
        else:
            skip_btn.click()
            logging.info("=====Click skip btn====")


def main():
    """test class Common"""
    driver = get_driver_()
    common = Common(driver)
    common.check_cancelBtn()
    common.check_skipBtn()


if __name__ == "__main__":
    main()
