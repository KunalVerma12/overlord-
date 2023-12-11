'''Dir function: The dir() function is a built-in-function that returns
a list of names in the current local scope or a list of attributes of
an object if passed as an argument. '''
'''time module: It returns the current time in seconds since the epoch
(the epoch is a predefined point in time, usually the beginning 
 of the year 1970) '''

'''import math
my_list=[1,2,3]
print("Attributes of a list: ",dir(my_list))
print("Attributes of a list: ",dir(math)) '''


import time
print("Start")
time.sleep(10) # Pauses execution for 10 seconds
print("End")
c=time.localtime(10)
print("Time: ",c)
