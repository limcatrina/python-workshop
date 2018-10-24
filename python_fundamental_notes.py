"""
Welcome to Notes for Python 

"""

import helloworld as hw 
from helloworld import * 	#import helloworld to use its functions immediately without having to use .

# creating list 
list1 = [0,1,2,3,4] #put 01234 into list 
if list1[4] == list1[-1]  # "-1" means the last element in the list 
	print("list has 4+1 elements")

# adding element abc to the end of the list 
list1.append("abc")

# pop the 0th array and save its element to prevfirstelement
prevfirstelement = list1.pop(0) 

#for iterating 
hw.helloworld(list1)  #helloworld is a function, carry out function for every item in list


# num is like a pointer in lsit1, starts from the first element to add 2 to it and prints then moves to the next element to carry out the addition and print 
for num in list1:
	num += 2
print list1

for i in range(x): # create a list of ascending integers starting from 0 goes to x-1
	print('cat is cat is cat is cat is cat')