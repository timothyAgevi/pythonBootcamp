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

# random on strings
#1 choice
friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.choice(friends_list))

# 2 sample -used to draw multiple choices
# cantains aurgument of how many
# only draws sample once
friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.sample(friends_list,3))


# 3 chaffle
import random
friends_list =  ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print(random.sample(friends_list,5))
random.shuffle(friends_list)
print(friends_list)