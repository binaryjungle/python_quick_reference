#Beginning of the program
print("Beginning Of the Program")
print("")

#Can see the philosophies of python using below import
import this
print("")

#import module from the library
import platform
print(platform.python_version())
print("")

import sys

#returns python version
print(sys.version_info)
print("")

#returns current operating system or platform
print(sys.platform)
print("")

import os

#returns version of the operating system
print(os.name)
print("")

#returns the value of PATH variable
print(os.getenv("PATH"))
print("")

#returns current workng directory
print(os.getcwd())
print("")

import random

#return some random number
print(random.randint(100, 200))
print("")

import datetime

#prints various date and time
sys_date = datetime.datetime.now()
print(sys_date)
print(sys_date.date())
print(sys_date.microsecond)
print(sys_date.time())

#End of the program
print("")
print("End Of the Program")