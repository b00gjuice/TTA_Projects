#!/usr/bin/python2.7
# Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59)
# Student: Freeman Cooley
# Python Course Item 64
# Drill: File Mover with Time Check
# https://docs.python.org/2/library/shutil.html
# https://www.tutorialspoint.com/python/python_date_time.htm
# Move text files from Folder_B to Folder_A

import shutil
import os
import random
import time
import sys

A = ("/Users/fcool/Desktop/Folder_A/")
B = ("/Users/fcool/Desktop/Folder_B/")

time.sleep(0.2)
print "Files in Folder_A", os.listdir(A)
time.sleep(0.2)
print "Files in Folder_B", os.listdir(B)
time.sleep(0.3)

def moveFiles(B, A):
    folder = os.listdir(B)
    for files in folder:
        old_timey = os.path.getmtime(B+files)
        time_check = time.time() - 86400
        if old_timey >= time_check:
            shutil.move(B+files, A)
            print os.path.abspath(A+files)

moveFiles(B, A)

time.sleep(0.2)
print "Files in Folder_A", os.listdir(A)
time.sleep(0.2)
print "Files in Folder_B", os.listdir(B)
time.sleep(0.3)
print "Text files moved from Folder_B to Folder_A"
