# -*-coding:utf-8 -*-
# File :setUp_tearDown.py
# Author:George
# Date : 2019/10/24
# motto: Someone always give up while someone always try!
"""basic unittest test case for encapsulation setUp and tearDown method, in teaching plan teacher used
driver.close_app() in tearDowm method """
import unittest
from time import sleep

from logging_driver_ import logging
from get_config import get_driver_


class Setup_tearDown(unittest.TestCase):
    def setUp(self):
        """
        give a default driver at basic test at a test setUp
        :return:
        """
        logging.info("=====SetUp=====")
        self.driver = get_driver_()

    def tearDown(self):
        """
        when finish a test case  close the app
        :return:
        """
        logging.info("=====TearDown=====")
        sleep(5)
        self.driver.close_app()
