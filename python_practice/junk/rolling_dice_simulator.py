from array import*
import random
my_array = array('i',[1,2,3,4,5,6])
je = input("Do you want to roll the dice? ")
if(je == 'y'):
 print(random.choice(my_array))
else:
 print("make better choice next time")
