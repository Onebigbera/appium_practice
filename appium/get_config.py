# -*-coding:utf-8 -*-
# File :get_config.py
# Author:George
# Date : 2019/10/24
# motto: Someone always give up while someone always try!
"""
    get config from yaml data
"""
import os
from appium import webdriver
import yaml
from logging_driver_ import logging


def get_driver_():
    """
    :return:
    """
    base_dir = os.path.dirname(os.path.dirname(__file__))
    print(base_dir)
    config_file = '/'.join([base_dir, 'appium', 'config',  'desired_capability.yaml'])
    print(config_file)
    with open(config_file, 'r') as f:
        config = yaml.load(f)
        desired_capability = {'platformName': config['platformName'],
                              'deviceName': config['deviceName'],
                              'app': config['app'],
                              'appPackage': config['appPackage'],
                              'appActivity': config['appActivity'],
                              # to recover previous settings
                              'noReset': config['noReset'],
                              # to set unicode  if used chinese
                              'unicodeKeyboard': config['unicodeKeyboard'],
                              # reset keyboard
                              'resetKeyboard': config['resetKeyboard']
                              }

        url = 'http' + '://' + str(config['ip']) + ":" + str(config['port']) + '/wd/hub'
        print(url)
        driver = webdriver.Remote(url, desired_capability)
        logging.info("=====starting app,please wait=====")
        # driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capability)
        driver.implicitly_wait(3)
        logging.info("=====wait to page refresh=====")
        return driver


if __name__ == "__main__":
    get_driver_()
