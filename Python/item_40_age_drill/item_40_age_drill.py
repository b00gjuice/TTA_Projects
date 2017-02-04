# Python v3.6.0:41df79263# Python v3.6.0:41df79263a11, Dec 23 2016
# Student: Freeman Cooley
# Python Course Item 40
# Calculate Age Drill
# Credit: http://www.wikihow.com/Create-a-Very-Simple-Program-in-Python
# Modified by Freeman Cooley

# Import time & sys for delays
import time
import sys

# vars for name and age
print("Let's see how long you have lived in days, minutes and seconds.")
name = input('name: ')
print ("now enter your age")
age = int(input("age:" ))

# Calculate age in days, minutes, seconds
days = age * 365
minutes = age * 525600
seconds = age * 31556926
time.sleep(0.2)

# display results in separate lines for easier reading
print(name, "has been alive for:\n", days, "days.\n", minutes, "minutes. \n and"
 , seconds, "seconds! \n Wow!")
time.sleep(0.1)
