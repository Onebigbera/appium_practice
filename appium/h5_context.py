# -*-coding:utf-8 -*-
# File :h5_context.py
# Author:George
# Date : 2019/10/23
# motto: Someone always give up while someone always try!
"""
    to show how to locate h5 element with context
"""
from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


def get_driver_xiaoyao():
    """

    :return:
    """
    desired_capability = {
        'platformName': 'Android',
        'platformVersion': '5.1.1',
        'deviceName': '127.0.0.1:21503',
        'app': r'F:\Appium\App\dr.fone3.2.0.apk',
        'appPackage': 'com.wondershare.drfone',
        'appActivity': 'com.wondershare.drfone.ui.activity.WelcomeActivity',
        # to recover previous settings
        'noReset': 'True',

        # to set unicode  if used chinese
        # 'unicodeKeyboard': "True",
        # reset keyboard
        # 'resetKeyboard': "True",
        # if you need recognition toast  set it
        # 'automationName': 'uiautomator2'

    }

    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capability)
    # in case of page do not show implicitly wait a moment
    driver.implicitly_wait(3)
    return driver


def locate_context(driver):
    """

    :param driver:
    :return:
    """
    print('click BackupBtn')
    driver.find_element_by_id('com.wondershare.drfone:id/btnBackup').click()

    WebDriverWait(driver, 8).until(lambda x: x.find_element_by_id('com.wondershare.drfone:id/btnRecoverData'))
    print('click NextBtn')
    driver.find_element_by_id('com.wondershare.drfone:id/btnRecoverData').click()

    WebDriverWait(driver, 8).until(lambda x: x.find_element_by_class_name('android.webkit.WebView'))

    # from android native to html
    contexts = driver.contexts
    print(contexts)

    # 需android4.4及以上版本的系统中才会输出更多的webview
    print('switch conetext')
    # 'WEBVIEW_com.wondershare.drfone' and 'NATIVE_APP' are in contexts
    driver.switch_to.context('WEBVIEW_com.wondershare.drfone')
    print('edit email')
    driver.find_element_by_id('email').send_keys('shuqing@wondershare.cn')
    print('click sendBtn')
    driver.find_element_by_class_name('btn_send').click()

    # 切换context 点击返回
    driver.switch_to.context('NATIVE_APP')
    driver.find_element_by_class_name('android.widget.ImageButton').click()


def main():
    """
    :return:
    """
    driver = get_driver_xiaoyao()
    locate_context(driver)


if __name__ == "__main__":
    main()
