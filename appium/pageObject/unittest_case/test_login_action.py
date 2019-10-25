# -*-coding:utf-8 -*-
# File :login_action.py
# Author:George
# Date : 2019/10/24
# motto: Someone always give up while someone always try!
"""
    logic business to encapsulation Login action
"""
from LoginView import LoginAction
from get_config import get_driver_
from logging_driver_ import logging
from pageObject.unittest_case.setUp_tearDown import Setup_tearDown


class TestLogin(Setup_tearDown):

    def test_login_george9526(self):
        logging.info("=====test login george9526=====")
        login_action = LoginAction(self.driver)
        login_action.login('george9526', 'george9526')

    def test_login_george9527(self):
        logging.info("=====test login george9527=====")
        login_action = LoginAction(self.driver)
        login_action.login('george9527', 'george9527')
        # self.assertEqual()

    def test_login_error(self):
        logging.info("=====test login error=====")
        login_action = LoginAction(self.driver)
        login_action.login('george9526', 'dsdfdf')


def main():
    test_login = TestLogin()
    test_login.test_login_george9527()


if __name__ == "__main__":
    main()
