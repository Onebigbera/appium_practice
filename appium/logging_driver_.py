# -*-coding:utf-8 -*-
# File :logging_driver_.py
# Author:George
# Date : 2019/10/24
# motto: Someone always give up while someone always try!
"""
    logging
"""

import logging.config

# CON_LOG = './config/log.conf'
CON_LOG = r'F:\Appium\Projects\appium_practice\appium\config\log.conf'
logging.config.fileConfig(CON_LOG)
logging = logging.getLogger()


# def get_logging():
#     """
#     :return:
#     """
#     import logging.config
#
#     CON_LOG = './config/log.conf'
#     logging.config.fileConfig(CON_LOG)
#     logging = logging.getLogger()
#     return logging
#
#
# if __name__ == "__main__":
#     get_logging()
