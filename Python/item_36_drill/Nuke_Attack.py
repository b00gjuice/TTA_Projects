# Python:       2.7.13
# Python Course Item 36 Drill
# Student:      Freeman Cooley
# For: The Tech Academy, Python Course, Item 36
# Date: 02/02/17

# Title: NUKE ATTACK!

# importing necessary modules
import random
import time
import sys

#Start of game
def start():
    country = get_country()
    nukes = get_nukes(country)
    time.sleep(0.5)
    printCount0()
    printCount1()
    printCount2()
    printCount3()
    time.sleep(0.5)
    text = "Countdown Begins! 10 9 8 7 6 5 4 3 2 1 LAUNCH!"
    for char in text:
        sys.stdout.write(char)
        time.sleep(0.1)
    print("\nHere are the results of your nuclear attack Mr. President:")
    time.sleep(0.5)
    print("\nThe Country attacked was: {}.".format(country))
    time.sleep(0.5)
    print("The Number of Missles launched was: {}.".format(nukes * 1))
    time.sleep(0.5)
    print("The Number of People killed was: {}.".format(nukes * 2000))
    time.sleep(0.5)
    print("The Number of Soldiers killed was: {}.".format(nukes * 700))
    time.sleep(0.5)
    print("The Number of Buildings destroyed was: {}.".format(nukes * 500))
    time.sleep(0.5)
    print("The Number of Military Aircraft destroyed was: {}.".format(nukes * 100))
    time.sleep(0.5)
    print("The Number of Military Vehicles destroyed was: {}.".format(nukes * 200))
    time.sleep(0.5)
    print("The Number of Ships destroyed was: {}.".format(nukes * 200))
    time.sleep(0.5)
    print("The Number of Submarines destroyed was: {}.".format(nukes * 100))
    time.sleep(0.5)
    print("The Number of Dogs destroyed was: {}.".format(nukes - 1))
    time.sleep(0.5)
    print("The Number of Cats destroyed was: {}.".format(nukes + 100000))
    time.sleep(0.5)
    print("The Number of visiting USA citizens destroyed was: {}.".format(nukes % 15))
    time.sleep(0.5)
    print("The Number of near misses was: {}.".format(nukes / 3))


# Choose what country to attack.

def get_country():
    stop = True
    while stop:
        country = raw_input("Good Morning Mr. President, who shall we nuke today?")

        # Defaults to random choice if user just hits "enter" key
        if(country == ''):
            country = random.choice('Russia China Syria DPRK Iran'.split())
            print("A random country will be attacked!")

        # USA is a prohibited choice
        if(country == "usa"):
            print("No-no Mr. President, we cannot attack our own country.")

        elif(country == "USA"):
            print("No-no Mr. President, we cannot attack our own country.")

        else:
            stop = False

    # country variable returned
    return country


# User Chooses number of Nukes to launch
def get_nukes(country):
    stop = True
    while stop:
        nukes = raw_input("Ha Ha {}! You are toast! How many Nukes shall we launch? ".format(country))

        # Chooses a random number of nukes if user just hits "enter" key
        if(nukes == ''):
            nukes = random.randint(11, 4999)
            print("{} nukes will be launched, Mr. President".format(nukes))

        # Demonstrating use of "and" operator
        if(int(nukes) == 1000) and (country == "Russia"):
            time.sleep(0.5)
            print("Russia + 1000 Nukes! Congratulations, you've earned a free trip to Las Vegas, NV. Mr. President")
            time.sleep(0.5)

        # Demonstrating use of "or" operator
        if(int(nukes) == 1) or (int(nukes) <= 10):
            time.sleep(0.5)
            print("What a wussy Mr. President! They will annihilate us in a counter-attack!")
            time.sleep(0.5)

        # Catch if user inputs 0 or greater than 5000
        if(int(nukes) == 0):
            print("Don't be a wuss, Mr. President. Launch those Nukes!")
        elif(int(nukes) > 5000):
            print("Umm...We don't have that many Nukes, Mr. President.")


        else:
            stop = False

    return int(nukes)

# Display a random binary effect for launch codes
# Example of usin a tuple
def countdown0():
    count = [ [0,1,0,0,1,0,1,0,0,1,1,1,0]
            ]
    return count

def printCount0():
    for i in countdown0():
        for a in i:
            time.sleep(0.1)
            print a,
        time.sleep(0.25)
        print "\n Launch code accepted. Thank You Mr. President"
        time.sleep(0.5)

def countdown1():
    count = [ [0,0,1,0,1,0,0,1,0,0,1,1,1]

            ]
    return count

def printCount1():
    for i in countdown1():
        for a in i:
            time.sleep(0.1)
            print a,
        time.sleep(0.25)
        print "\n Launch code accepted. Thank You Mr. Vice President"
        time.sleep(0.5)

def countdown2():
    count = [ [1,0,0,0,1,0,0,1,0,0,1,0,1]

            ]
    return count

def printCount2():
    for i in countdown2():
        for a in i:
            time.sleep(0.1)
            print a,
        time.sleep(0.25)
        print "\n Launch code accepted. Thank You Mr. Secretary"
        time.sleep(0.5)

def countdown3():
    count = [ [1,1,1,0,1,0,0,1,0,0,1,0,0]

            ]
    return count

def printCount3():
    for i in countdown3():
        for a in i:
            time.sleep(0.1)
            print a,
        time.sleep(0.25)
        print "\n Launch code accepted. Thank You Mr. Chief of Staff"
        time.sleep(0.5)

if __name__ == "__main__":
    start()
