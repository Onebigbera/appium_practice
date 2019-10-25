# -*-coding:utf-8 -*-
# File :kaoyanbang.py
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