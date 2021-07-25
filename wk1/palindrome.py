#project Euler #4 - largest palindrome of two 3 - digit numbers 
# a palindrome is a number that is the same backwards and forwards,
#  like 101 or 990099

import time
# find all palindromes between 100 and 999
def is_palindrome(val):
    val = str(val) # convert the value to string
    if val == val[::-1]:
        return(True)
    else:
        return(False)

# def is_palindrome(val):
#     return str(val) == str(val)[::-1]

# brute force approach
# step 1:take all 3 digit numbers and multiply by themself
# i.e 100 * 100,100 * 101 ...
def palindrome():
    start_time = time.time()
    palindromes_list=[]
    debug_list=[]
    low_val =10
    high_val = 40
    iterations = 0
    for num1 in range(low_val,high_val):
        for num2 in range(low_val,high_val):
            iterations += 1
       
        if is_palindrome(num1*num2):
                palindromes_list.append(num1*num2)
                debug_list.append([num1,num2,num1*num2])
    print('print of palindromes:',palindromes_list, num1, num2)
    print('debug_list:', debug_list)
    print('Iterations:' , iterations)
    print('Largest palindrome:', max(palindromes_list))
    print('Runtime:', time.time()-start_time)
    print('---------End Run--------')

palindrome()    
