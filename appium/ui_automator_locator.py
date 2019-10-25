# -*-coding:utf-8 -*-
# File :ui_automator_locator.py
# Author:George
# Date : 2019/10/23
# motto: Someone always give up while someone always try!

from get_driver import get_driver
from kyb_basic import tap_cancel_button


def ui_automator_locate(dirver):
    """

    :param dirver:
    :return:
    """
    dirver.find_element_by_android_uiautomator \
        ('new UiSelector().resourceId("com.tal.kaoyan:id/login_email_edittext")').send_keys('zxw1234')

    # locate with text property
    # dirver.find_element_by_android_uiautomator \
    # ('new UiSelector().text("请输入用户名")').send_keys('zxw1234')

    # localte with className
    dirver.find_element_by_android_uiautomator \
        ('new UiSelector().className("android.widget.EditText")').send_keys('zxw1234')

    dirver.find_element_by_android_uiautomator \
        ('new UiSelector().resourceId("com.tal.kaoyan:id/login_password_edittext")').send_keys('zxw123456')

    dirver.find_element_by_android_uiautomator \
        ('new UiSelector().resourceId("com.tal.kaoyan:id/login_login_btn")').click()


def main():
    driver = get_driver()
    tap_cancel_button(driver)
    ui_automator_locate(driver)


if __name__ == "__main__":
    main()
