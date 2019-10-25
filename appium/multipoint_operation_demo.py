# -*-coding:utf-8 -*-
# File :mutipoint_operation.py
# Author:George
# Date : 2019/10/24
# motto: Someone always give up while someone always try!
"""
    multipoint operation
"""
from appium import webdriver
from appium.webdriver.common.multi_action import MultiAction
from appium.webdriver.common.touch_action import TouchAction
from selenium.common.exceptions import NoSuchElementException


def get_driver():
    """
    launch an app with basic desired_capability
    :return:
    """
    # desired_capability dictionary
    # simulator  Night God simulator
    desired_capability = {'platformName': 'Android',
                          'deviceName': '127.0.0.1:62025',
                          'app': r'F:\Appium\App\com.baidu.BaiduMap.apk',
                          'appPackage': 'com.baidu.BaiduMap',
                          'appActivity': 'com.baidu.baidumaps.WelcomeScreen',
                          # to recover previous settings
                          'noReset': 'True',

                          # to set unicode  if used chinese
                          'unicodeKeyboard': "True",

                          # reset keyboard
                          'resetKeyboard': "True",
                          # if you need recognition toast  set it
                          'automationName': 'uiautomator2'

                          }

    # phone
    # desired_cupability_phone = {
    #     # phone name
    #     'deviceName': 'MX4',
    #     # android version of phone
    #     'platVersion': '5.1',
    #     # you can get it form adb devices order
    #     'udid': '750dsd454fd5',
    #
    #     'app': r'F:\Appium\App\kaoyan3.1.0.apk',
    #     'appPackage': 'com.tal.kaoyan',
    #     'appActivity': 'com.tal.kaoyan.ui.activity.SplashActivity'
    # }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capability)
    # in case of page do not show implicitly wait a moment
    driver.implicitly_wait(3)
    return driver


def zoom_action_demo(driver):
    """

    :param driver:
    :return:
    """
    driver.find_element_by_id('com.baidu.BaiduMap:id/dj2').click()
    driver.find_element_by_id('com.baidu.BaiduMap:id/byo').click()
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']

    action1 = TouchAction(driver)
    action2 = TouchAction(driver)

    zoom_action = MultiAction(driver)

    action1.press(x=x*0.4, y=y*0.4).wait(1000).move_to(x=x*0.2, y=y*0.2).wait(1000).release()
    action2.press(x=x*0.6, y=y*0.6).wait(1000).move_to(x=x*0.8, y=y*0.8).wait(1000).release()

    print("start zoom action...")
    # multiAction to load independent action
    zoom_action.add(action1, action2)
    zoom_action.perform()


def pinch_action(driver):
    """

    :param driver:
    :return:
    """
    driver.implicitly_wait(3)
    try:
        choose_button = driver.find_element_by_id("com.baidu.BaiduMap:id/dj2")
        choose_button.click()
    except NoSuchElementException:
        print("Images choose element does not exists...")

    try:
        choose_button2 = driver.find_element_by_id("com.baidu.BaiduMap:id/byo")
        choose_button2.click()
    except NoSuchElementException:
        print("Images choose element does not exists...")

    action1 = TouchAction(driver)
    action2 = TouchAction(driver)
    zoom_action = MultiAction(driver)

    # get screen size relative position usage
    x = driver.get_window_size()['width']
    y = driver.get_window_size()['height']

    action1.press(x=x*0.2, y=y*0.2).wait(1000).move_to(x=x*0.4, y=y*0.4).wait(1000).release()
    action2.press(x=x*0.8, y=y*0.8).wait(1000).move_to(x=x*0.6, y=y*0.6).wait(1000).release()
    print("start to pinch...")
    zoom_action.add(action1, action2)
    zoom_action.perform()


def main():
    driver = get_driver()
    for i in range(3):
        pinch_action(driver)
        # zoom_action_demo(driver)


if __name__ == "__main__":
    main()
