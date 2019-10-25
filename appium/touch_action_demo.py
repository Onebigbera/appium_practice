# -*-coding:utf-8 -*-
# File :touch_action_demo.py
# Author:George
# Date : 2019/10/24
# motto: Someone always give up while someone always try!
"""
    serious action
"""
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from time import sleep


def driver_config():
    """
    config of test app
    :return:
    """
    desired_capability = {'platformName': 'Android',
                          'deviceName': '127.0.0.1:62025',
                          'app': r'F:\Appium\App\mymoney.apk',
                          'appPackage': 'com.mymoney',
                          'appActivity': 'com.mymoney.biz.splash.SplashScreenActivity',
                          # to recover previous settings
                          'noReset': 'True',

                          # to set unicode  if used chinese
                          'unicodeKeyboard': "True",

                          # reset keyboard
                          'resetKeyboard': "True",
                          # if you need recognition toast  set it
                          'automationName': 'uiautomator2'
                          }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capability)
    # in case of page do not show implicitly wait a moment
    driver.implicitly_wait(3)
    return driver


def get_size(driver):
    """
    get size of the screen
    :param driver:
    :return:
    """
    x = driver.get_window_size()["width"]
    y = driver.get_window_size()["height"]
    return x, y


def swipeLeft(driver):
    """

    :param driver:
    :return:
    """
    coordinate = get_size(driver)
    x1 = int(coordinate[0] * 0.9)
    y1 = int(coordinate[1] * 0.5)
    x2 = int(coordinate[0] * 0.1)
    driver.swipe(x1, y1, x2, y1, 1000)


def swipeUp(driver):
    """

    :param driver:
    :return:
    """
    coordinate = get_size(driver)
    x1 = int(coordinate[0] * 0.5)
    y1 = int(coordinate[1] * 0.95)
    y2 = int(coordinate[1] * 0.35)
    driver.swipe(x1, y1, x1, y2, 1000)


def launch_page(driver):
    """

    :param driver:
    :return:
    """

    # judge whether there is a advertising if there is then close it
    try:
        closBtn = driver.find_element_by_id('com.mymoney:id/close_iv')
    except NoSuchElementException:
        print("No advertising")
        pass
    else:
        closBtn.click()

    try:
        next_step = driver.find_element_by_id('com.mymoney:id/next_btn')
    except NoSuchElementException:
        print("Next step button is not in the page...")
        pass
    else:
        next_step.click()

    swipeLeft(driver)

    try:
        begin_button = driver.find_element_by_id('com.mymoney:id/begin_btn')
    except NoSuchElementException:
        print("开启随手记 button is not in the page...")
        pass
    else:
        begin_button.click()

    try:
        set_button = driver.find_element_by_id('com.mymoney:id/nav_setting_btn')
    except NoSuchElementException:
        print("更多 button is not in the page...")
        pass
    else:
        set_button.click()

    WebDriverWait(driver, 6).until(lambda x: x.find_element_by_id("com.mymoney:id/accbook_member_head_iv"))
    swipeUp(driver)
    # id/xpath/ui automator
    driver.find_element_by_android_uiautomator('new UiSelector().text("高级")').click()

    try:
        gesture_button = driver.find_element_by_id('com.mymoney:id/password_protected_briv')
    except NoSuchElementException:
        print("密码与手势密码 button is not in the page...")
        pass
    else:
        gesture_button.click()

    sleep(3)

    try:
        gesture_button = driver.find_element_by_id('com.mymoney:id/lock_pattern_or_not_sriv')
    except NoSuchElementException:
        print("手势密码保护 button is not in the page...")
        pass
    else:
        gesture_button.click()

    # series action  action chain todo: while to soduku operate it always shows the same route!!
    for i in range(2):
        TouchAction(driver).press(x=243, y=375).wait(2000) \
            .move_to(x=432, y=375).wait(2000) \
            .move_to(x=655, y=375).wait(2000) \
            .move_to(x=655, y=583).wait(2000) \
            .move_to(x=655, y=775).wait(2000) \
            .release().perform()
        sleep(2)


def main():
    driver = driver_config()
    launch_page(driver)


if __name__ == "__main__":
    main()
