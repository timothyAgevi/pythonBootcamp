#Use Python script to generate a random password of 8 characters.
#  Each time the program is run,
#  a new password will be generated randomly. 
# The passwords generated will be 8 characters long
#  and will have to include the following characters in any order:

# 2 uppercase letters from A to Z,
# 2 lowercase letters from a to z,
# 2 digits from 0 to 9,
# 2 punctuation signs such as !, ?, “, # etc.

# Hint: To solve this challenge we will have to generate random characters and to do so we will need to use the ASCII code.

# solution 

import random


uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = uppercase_letters.lower()
digits = "0123456789"
symbols = "(){}[]/,.<>`'\\|#* "

upper, lower, nums, syms = True, True, True, True

# string containing everything that we are going to use
all = ""

if upper:
    all += uppercase_letters

if lower:
    all += lowercase_letters

if nums:
    all += digits

if syms:
    all += symbols

length = 8
amount = 10


for x in range(amount):
    password = "".join(random.sample(all, length))
    print (password)