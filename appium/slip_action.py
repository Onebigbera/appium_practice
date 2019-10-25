# -*-coding:utf-8 -*-
# File :slip_action.py
# Author:George
# Date : 2019/10/23
# motto: Someone always give up while someone always try!
"""
    slip action
"""
from time import sleep

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from get_driver import get_driver


def get_size(driver):
    """
    get the whole size of screen as a whole part return (x, y)
    :param driver:
    :return:
    """
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']
    print(x, y)
    return x, y


def slipLeft(driver):
    """
    slip action
    :param driver:
    :return:
    """
    coordinate = get_size(driver)
    x1 = int(coordinate[0] * 0.9)
    y1 = int(coordinate[1] * 0.5)
    x2 = int(coordinate[0] * 0.1)

    driver.swipe(x1, y1, x2, y1, 1000)


def slipUp(driver):
    """
    slip action
    :param driver:
    :return:
    """
    coordinate = get_size(driver)
    x1 = int(coordinate[0] * 0.5)
    y1 = int(coordinate[1] * 0.95)
    y2 = int(coordinate[1] * 0.35)

    driver.swipe(x1, y1, x1, y2, 1000)


def slip_action(driver):
    """

    :return:
    """
    # whether need to update
    try:
        cancel_button = driver.find_element_by_id("android:id/button2")
        cancel_button.click()
        print("Clicked cancel button...")
    except NoSuchElementException:
        print("Cancel button does not exist in web page")

    # explicitly wait

    for i in range(2):
        slipLeft(driver)
        sleep(2)
    WebDriverWait(driver, 3).until(lambda x: x.find_element_by_id("com.tal.kaoyan:id/activity_splash_guidfinish"))
    driver.find_element_by_id('com.tal.kaoyan:id/activity_splash_guidfinish').click()
    print("Welcome to login page...")


def touch_action(driver):
    """
    touch action with a series action
    :param driver:
    :return:
    """


def main():
    driver = get_driver()
    slip_action(driver)


if __name__ == "__main__":
    main()
