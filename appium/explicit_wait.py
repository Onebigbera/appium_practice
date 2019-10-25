# -*-coding:utf-8 -*-
# File :explicit_wait.py
# Author:George
# Date : 2019/10/23
# motto: Someone always give up while someone always try!
from get_driver import get_driver
from kyb_basic import tap_cancel_button
from selenium.webdriver.support.ui import WebDriverWait


def explicit_wait_demo(driver):
    """
    explicit wait demo the same like selenium webdriver explicit driver
    :return:
    """
    tap_cancel_button(driver)
    # the parameter of lambda function is dynamic and there it stands for driver  lambda function is useful
    WebDriverWait(driver, 3, 0.5).until(lambda x: x.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum'))
    driver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_forum').click()


def main():
    driver = get_driver()
    explicit_wait_demo(driver)


if __name__ == "__main__":
    main()
