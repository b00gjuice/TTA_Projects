# Python v3.6.0:41df79263# Python v3.6.0:41df79263a11, Dec 23 2016
# Student: Freeman Cooley
# Python Course Item 48
# DRILL: Python Sort Drill
# Study Pages:
# https://wiki.python.org/moin/HowTo/Sorting
# http://www.compciv.org/guides/python/fundamentals/sorting-collections-with-sorted/
# https://docs.python.org/3/howto/sorting.html
# http://stackoverflow.com/questions/11964450/python-order-a-list-of-numbers-without-built-in-sort-min-max-function

# Sort Drill Part 1

def sortFunc (sort_listA):

# Using Range to iterate through the list, start, stop, step.

    for x in range(len(sort_listA)-1,0,-1):
# Using a nested for loop to calculate to sorting
        for y in range(x):
            if num_listA[y]>sort_listA[y+1]:
                sort_listA[y], sort_listA[y+1] = sort_listA[y+1], sort_listA[y]

# TTA list to be sorted
num_listA = [67, 45, 2, 13, 1, 998]

# Use Sort Function to order list
sortFunc(num_listA)
print("\nSort Drill List 1:")
print(num_listA)

# Sort Drill Part 2

def sortFunc (sort_listB):

# Using Range to iterate through the list, start, stop, step.

    for x in range(len(sort_listB)-1,0,-1):
# Using a nested for loop to calculate to sorting
        for y in range(x):
            if num_listB[y]>sort_listB[y+1]:
                sort_listB[y], sort_listB[y+1] = sort_listB[y+1], sort_listB[y]

# TTA list to be sorted
num_listB = [89, 23, 33, 45, 10, 12, 45, 45, 45]

# Use Sort Function to order list
sortFunc(num_listB)
print("\nSort Drill List 2:")
print(num_listB)
