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

def is_palindrome(val):
    return str(val) == str(val)[::-1]