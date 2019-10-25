# -*-coding:utf-8 -*-
# File :screenshot.py
# Author:George
# Date : 2019/10/23
# motto: Someone always give up while someone always try!
"""
    screen_shot in appium
"""
from get_driver import get_driver
from kyb_basic import tap_cancel_button


def screen_shot_demo(driver):
    """

    :param driver:
    :return:
    """
    image_path = './screenshot/login.png'

    # method 1
    # driver.save_screenshot(image_path)

    # method 2
    driver.get_screenshot_as_file(image_path)


def main():
    driver = get_driver()
    tap_cancel_button(driver)
    screen_shot_demo(driver)


if __name__ == "__main__":
    main()
