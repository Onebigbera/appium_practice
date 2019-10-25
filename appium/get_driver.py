# -*-coding:utf-8 -*-
# File :get_driver.py
# Author:George
# Date : 2019/10/23
# motto: Someone always give up while someone always try!
"""
    driver module,insure your project configured properly
"""
from appium import webdriver


def get_driver():
    """
    launch an app with basic desired_capability
    :return:
    """
    # desired_capability dictionary
    # simulator  Night God simulator
    desired_capability = {'platformName': 'Android',
                          'deviceName': '127.0.0.1:62025',
                          'app': r'F:\Appium\App\kaoyan3.1.0.apk',
                          'appPackage': 'com.tal.kaoyan',
                          'appActivity': 'com.tal.kaoyan.ui.activity.SplashActivity',
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
