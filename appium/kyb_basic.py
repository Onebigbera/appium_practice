# -*-coding:utf-8 -*-
# File :kyb.py
# Author:George
# Date : 2019/10/22
# motto: Someone always give up while someone always try!
"""
    First appium script
"""
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException


def launch_app():
    """
    launch an app with basic desired_cupability
    :return:
    """
    # desired_capability dictionary
    # simulator
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
                          'resetKeyboard': "True"
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
    driver.implicitly_wait(5)
    return driver


def tap_cancel_button(driver):
    """
    location by id
    driver: driver instance
    :return:
    """
    # search cancel button by is and click it  but you should judge it whether exists
    try:
        cancel_button = driver.find_element_by_id("android:id/button2")
        cancel_button.click()
        print("Clicked cancel button...")
    except NoSuchElementException:
        print("Cancel button does not exist in web page")

    # search skip button and exception capture if not exists
    try:
        cancel_button = driver.find_element_by_id("com.tal.kaoyan:id/tv_skip")
        cancel_button.click()
        print("Clicked skip button...")
    except NoSuchElementException:
        print("Skip button does not exist in web page")
        driver.implicitly_wait(3)


def login_action(driver):
    """
    driver instance
    :param driver:
    :return:
    """
    try:
        # account_button = driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext")
        # locate by className todo class name locator
        account_button = driver.find_element_by_class_name("android.widget.EditText")
        account_button.clear()
        account_button.send_keys('george9527')
    except NoSuchElementException:
        print("Does not locate account element...")

    try:
        password_button = driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext")
        password_button.clear()
        password_button.send_keys("george9527")
    except NoSuchElementException:
        print("Does not locate password element...")
    try:
        action_button = driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn")
        action_button.click()
    except NoSuchElementException:
        print("Locate element does not exists")
    print("congratulation!Login successfully...")


def login_action_xpath(driver):
    """

    :param driver:
    :return:
    """
    print("Login with xpath location...")
    try:
        # account_button = driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext")
        # locate by className todo: xpath selector
        account_button = driver.find_element_by_xpath("//android.widget.EditText[@text='请输入用户名']")
        # account_button = driver.find_element_by_xpath("//android.widget.EditText[@id='com.tal.kaoyan:id/login_email_edittext']")
        # todo: there is a bug we can locate the account element by id and text property but we can not locate it
        #  with id property in xpath locator account_button = driver.find_element_by_xpath("//*[
        #  @id='com.tal.kaoyan:id/login_email_edittext']")
        account_button.clear()
        account_button.send_keys('george9527')
    except NoSuchElementException:
        print("Does not locate account element...")

    try:
        password_button = driver.find_element_by_xpath("//android.widget.EditText[@class='android.widget.EditText' and @index='3']")
        password_button.clear()
        password_button.send_keys("george9527")
    except NoSuchElementException:
        print("Does not locate password element...")

    try:
        action_button = driver.find_element_by_xpath("//*[@class='android.widget.Button']")
        action_button.click()
    except NoSuchElementException:
        print("Locate element does not exists")
    print("congratulation!Login successfully...")


def repeat_login(driver):
    """

    :param driver:
    :return:
    """
    try:
        user_button = driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl")
        user_button.click()
    except NoSuchElementException:
        print("User button does not exist...")

    try:
        login_button = driver.find_element_by_id("com.tal.kaoyan:id/activity_usercenter_userheader")
        login_button.click()
    except NoSuchElementException:
        print("Login element does not exist...")
    login_action(driver)


def relative_positioning(driver):
    """
    relative_positioning  parent element is the above level
    :param driver:
    :return:
    """
    # parent element
    try:
        parent_element = driver.find_element_by_id("com.tal.kaoyan:id/activity_register_scrollview")
        # embedded logic
        try:
            sub_element = parent_element.find_element_by_class_name("android.widget.ImageView")
            sub_element.click()
        except NoSuchElementException:
            print("Login element does not exist...")
    except NoSuchElementException:
        print("User button does not exist...")


def user_choice_image(driver):
    """
    choose image for user by list method
    :return:
    """
    try:
        register_button = driver.find_element_by_id("com.tal.kaoyan:id/login_register_text")
        register_button.click()
    except NoSuchElementException:
        print("Register element does not exists...")
    driver.implicitly_wait(3)

    try:
        images_choose_button = driver.find_element_by_id("com.tal.kaoyan:id/activity_register_userheader")
        images_choose_button.click()
    except NoSuchElementException:
        print("Images choose element does not exists...")

    try:
        images = driver.find_elements_by_id("com.tal.kaoyan:id/item_image")
        images[2].click()
    except NoSuchElementException:
        print("Images choose element does not exists...")

    try:
        save_button = driver.find_element_by_id("com.tal.kaoyan:id/save")
        save_button.click()
    except NoSuchElementException:
        print("Save button does not exists...")


def skip_register_page(driver):
    """

    :param driver:
    :return:

    """
    try:
        user_button = driver.find_element_by_id("com.tal.kaoyan:id/mainactivity_button_mysefl")
        user_button.click()
    except NoSuchElementException:
        print("User button does not exist...")

    try:
        login_button = driver.find_element_by_id("com.tal.kaoyan:id/activity_usercenter_userheader")
        login_button.click()
    except NoSuchElementException:
        print("Login element does not exist...")


def main():
    driver = launch_app()
    tap_cancel_button(driver)
    skip_register_page(driver)
    user_choice_image(driver)
    # login_action(driver)
    # login_action_xpath(driver)
    # repeat_login(driver)


if __name__ == "__main__":
    main()



