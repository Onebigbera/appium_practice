# -*-coding:utf-8 -*-
# File :toast_discern.py
# Author:George
# Date : 2019/10/23
# motto: Someone always give up while someone always try!
"""
    toast discern
"""
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

from get_driver import get_driver
from kyb_basic import tap_cancel_button


def toast_discern(driver):
    """

    :param driver:
    :return:
    """
    try:
        # account_button = driver.find_element_by_id("com.tal.kaoyan:id/login_email_edittext")
        # locate by className todo class name locator
        account_button = driver.find_element_by_class_name("android.widget.EditText")
        account_button.clear()
        account_button.send_keys('george9527ds')
    except NoSuchElementException:
        print("Does not locate account element...")

    try:
        password_button = driver.find_element_by_id("com.tal.kaoyan:id/login_password_edittext")
        password_button.clear()
        password_button.send_keys("george9527ds")
    except NoSuchElementException:
        print("Does not locate password element...")
    try:
        action_button = driver.find_element_by_id("com.tal.kaoyan:id/login_login_btn")
        action_button.click()
    except NoSuchElementException:
        print("Locate element does not exists")
    print("congratulation!Login successfully...")

    # error_message = "用户名或密码错误，你还可以尝试4次"
    error_message = "账号不存在"
    limit_message = "验证失败次数过多，请15分钟后再试"

    # reverse lookup
    error_message_xpath = "//*[@text='{}']".format(error_message)
    toast_element = WebDriverWait(driver, 5).until(lambda x: x.find_element_by_xpath(error_message_xpath))
    print(toast_element.text)


def main():
    driver = get_driver()
    tap_cancel_button(driver)
    toast_discern(driver)
    pass


if __name__ == "__main__":
    main()
