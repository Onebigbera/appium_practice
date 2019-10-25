# -*-coding:utf-8 -*-
# File :kyb_login.py
# Author:George
# Date : 2019/10/21
# motto: Someone always give up while someone always try!
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md

print("Connect devices...")
device = mr.waitForConnection()

print("Install app...")
device.installPackage(r"F:\Appium\App\kaoyan3.1.0.apk")

print("Launch app...")
package = 'com.tal.kaoyan'
activity = 'com.tal.kaoyan.ui.activity.SplashActivity'
runComponent = package + '/' + activity

device.startActivity(component=runComponent)
mr.sleep(3)

print("Touch cancel button...")
device.touch(637, 942, 'DOWN_AND_UP')
mr.sleep(2)

print("Touch skip button...")
device.touch(799, 67, "DOWN_AND_UP")
mr.sleep(2)

print("input username......")
device.touch(117, 365, 'DOWN_AND_UP')
username = 'george9527'
device.type(username)
mr.sleep(1)

print("input password......")
device.touch(118, 476, 'DOWN_AND_UP')
password = 'george9527'
device.type(password)
mr.sleep(3)

print("touch login button......")
device.touch(453, 629, 'DOWN_AND_UP')
mr.sleep(1)

print("Take snapshot...")
screenshot = device.takeSnapshot()
screenshot.writeToFile(r'F:\Appium\logs\screenShot\kyb.png')