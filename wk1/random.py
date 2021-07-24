# basic syntax
import random   

print(random.random()) 
 # error : TypeError: 'module' object is not callable

# to display 5 numbers  btn 0 and 1
# for i in range(5):
#     print(random.random())

# to display 5 numbers  upto 6
for i in range(5):
    print(random.random()* 6)

# using uniform 
# 2 parameters ;num to statr from ;number to end
for i in range(5):
    print(random.uniform(1,6))

# for just integers use rand int    
for i in range(5):
    print(random.int(1,6))

# use of ranrange(), add 3rd parameter : step
for i in range(5):
    print(random.randrange(1,6,3))