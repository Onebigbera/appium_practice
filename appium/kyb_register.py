# -*-coding:utf-8 -*-
# File :kyb_register.py
# Author:George
# Date : 2019/10/23
# motto: Someone always give up while someone always try!
"""
    user register model
        user account password
        image choice
        object choice
        without verification code
        we can cancel verification code in development
"""
import random

from selenium.common.exceptions import NoSuchElementException
from get_driver import get_driver


def register_kyb(driver):
    """

    :param driver:
    :return:
    """

    # check whether to update and advertising
    print("Check whether to update and pass advertising...")
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

    # set user image
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

    # set user account and password and email
    try:
        user_account = driver.find_element_by_id("com.tal.kaoyan:id/activity_register_username_edittext")
        user_account.clear()
        account = "george" + str(random.randint(5000, 9000))
        user_account.send_keys(account)
        print("account is {}".format(account))
    except NoSuchElementException:
        print("User account does not exists...")
    try:
        user_password = driver.find_element_by_id("com.tal.kaoyan:id/activity_register_password_edittext")
        user_password.clear()
        password = "george" + str(random.randint(5000, 9000))
        user_password.send_keys(password)
        print("password is {}".format(password))
    except NoSuchElementException:
        print("Password button does not exists...")

    try:
        user_email = driver.find_element_by_id("com.tal.kaoyan:id/activity_register_email_edittext")
        user_email.clear()
        email = "george" + str(random.randint(5000, 9000)) + "@qq.com"
        user_email.send_keys(email)
        print("email is {}".format(email))
    except NoSuchElementException:
        print("Email button does not exists...")

    try:
        register_btn = driver.find_element_by_id("com.tal.kaoyan:id/activity_register_register_btn")
        register_btn.click()
        print("register successfully")
    except NoSuchElementException:
        print("register button does not exists...")

    # set personal info
    try:
        year_btn = driver.find_element_by_id("com.tal.kaoyan:id/activity_perfectinfomation_time")
        year_btn.click()
        print("click year btn")
    except NoSuchElementException:
        print("year button does not exists...")

    try:
        years = driver.find_elements_by_id("android:id/text1")
        years[2].click()
        print("Choose second year choice")
    except NoSuchElementException:
        print("year choice does not exists...")

    try:
        school = driver.find_element_by_id("com.tal.kaoyan:id/perfectinfomation_edit_school_name")
        school.click()
        print("Click school  choice")
    except NoSuchElementException:
        print("School choice does not exists...")

    try:
        school_choices = driver.find_elements_by_id("com.tal.kaoyan:id/more_forum_title")
        school_choices[1].click()
        print("Click school  choice")
    except NoSuchElementException:
        print("School choice does not exists...")

    try:
        school_choices = driver.find_elements_by_id("com.tal.kaoyan:id/university_search_item_name")
        school_choices[2].click()
        print("Click detail school ")
    except NoSuchElementException:
        print("School choice does not exists...")
        driver.implicitly_wait(2)

    try:
        school = driver.find_element_by_id("com.tal.kaoyan:id/activity_perfectinfomation_major")
        school.click()
        print("Click major  choice")
    except NoSuchElementException:
        print("School choice does not exists...")

    try:
        major_choices = driver.find_elements_by_id("com.tal.kaoyan:id/major_subject_title")
        major_choices[3].click()
        print("Click major choice ")
    except NoSuchElementException:
        print("Major choice does not exists...")

    try:
        major_choices = driver.find_elements_by_id("com.tal.kaoyan:id/major_group_title")
        major_choices[2].click()
        print("Click major choice detail ")
    except NoSuchElementException:
        print("Major choice does not exists...")

    try:
        major_choices = driver.find_elements_by_id("com.tal.kaoyan:id/major_search_item_name")
        major_choices[2].click()
        print("Click major choice detail ")
    except NoSuchElementException:
        print("Major choice does not exists...")

    try:
        go_btn = driver.find_element_by_id("com.tal.kaoyan:id/activity_perfectinfomation_goBtn")
        go_btn.click()
        print("Click to come in ")
        print("Congratulation,register successfully...")
    except NoSuchElementException:
        print("Come in choice does not exists...")


def main():
    driver = get_driver()
    register_kyb(driver)


if __name__ == "__main__":
    main()
