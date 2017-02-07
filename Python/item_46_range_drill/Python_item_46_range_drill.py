# Python v3.6.0:41df79263# Python v3.6.0:41df79263a11, Dec 23 2016
# Student: Freeman Cooley
# Python Course Item 46
# DRILL: Python range function
# Study Page: http://pythoncentral.io/pythons-range-function-explained/

# DRILL PART 1
# Using Range Function + One Parameter to Print 0-3 using for method
fc_num_list = ['0', '1', '2','3',] # the comma after 3 allows for display in Atom script shell
print("Drill 1: Using Range Function + One Parameter to print 0-3")
for a in range(4):
    print(fc_num_list[a])

# Using Range Function + One Parameter to Print 0-3 by iterating list with len
fc_num_list = ['0', '1', '2','3',]
fc_num_list_len = len(fc_num_list)
print("Drill 1: Using Range Function + One Parameter to Print 0-3 by iterating list with len")
for a in range(0, fc_num_list_len):
    print(fc_num_list[a])

#DRILL PART 2
# Using Range Function + One Parameter to Print 0-3 using for method
fc_num_list = ['0', '1', '2','3',] # the comma after 3 allows for display in Atom script shell
print("Drill 2: Using Range Function + One Parameter to print 3-0")
for a in range(3, -1, -1,):
    print(fc_num_list[a])

# Using Range Function + Three Parameters to Print 3-0 by iterating list with len in reverse
fc_num_list = ['0', '1', '2','3',]
fc_num_list_len = len(fc_num_list)
print("Drill 2: Using Range Function + Three Parameters to Print 3-0 by iterating list with len in reverse")
for a in range(0, fc_num_list_len):
    print(fc_num_list[::-1][a]) #using [::-1] prints results in reverse

#DRILL PART 3

# Using Range Function + Three Parameters to Print 8 6 4 2 using for method
fc_num_list = ['0', '1', '2','3','4', '5', '6', '7', '8',]
print("Drill 3: Using Range Function + Three Parameters to Print 8 6 4 2")
for a in range(8, 0, -2):
    print(fc_num_list[a])
