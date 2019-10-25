# -*-coding:utf-8 -*-
# File :baseView.py
# Author:George
# Date : 2019/10/24
# motto: Someone always give up while someone always try!
"""
    Base view  the basic page class
"""


class BaseView(object):
    """
    BaseView of page class
    """

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, *loc):
        """
        invoke the driver method but not method itself
        :param loc:
        :return:
        """
        return self.driver.find_element(*loc)


