#!/usr/bin/python2.7
# Python 2.7.13 (v2.7.13:a06454b1afa1, Dec 17 2016, 20:42:59)
# Student: Freeman Cooley
# Python Course Item 62
# Drill: Pydrill_Datetime_27_idle
# http://stackoverflow.com/questions/13866926/python-pytz-list-of-timezones
# http://www.guru99.com/date-time-and-datetime-classes-in-python.html


# importing modules
import time
import datetime
from datetime import timedelta

# Determining time
Portland = datetime.datetime.now()
London = datetime.datetime.now() + timedelta(hours=8)
NYC = datetime.datetime.now() + timedelta(hours=3)

# Printing Current time at all 3 locations
print "Portland Time: ", Portland
print "London Time: ", London
print "New York City Time: ", NYC

# Printing out "Open" or "Closed" depending on time comparison
if London.time() > datetime.time(9,0,0,0) and London.time() < datetime.time(21,0,0,0):
    print ("London Branch is Open")
else:
    print ("London Branch is Closed")

if NYC.time() > datetime.time(9,0,0,0) and NYC.time() < datetime.time(21,0,0,0):
    print ("NYC Branch is Open")
else:
    print ("NYC Branch is Closed")
