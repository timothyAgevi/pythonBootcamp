def palindrome_create():
    nums=('9','8','7','6','5','4','3','2','1','0') # we create a list of the strings we will use
    iterations = 0 # we bring along our trusty iterator
    
    for dig in range(10):
        for dig1 in range(10):
            for dig2 in range(10):
                #we create the palindrome string by slicing using the iterators
                pal_str = nums[dig] + nums[dig1] + nums[dig2] + nums[dig2] + nums[dig1] +nums[dig]  
                palindrome = int(pal_str) # typecast string into an integer
                # print(pal_str, palindrome) #debug to check palindromes tested
                
                #lowest number to check against that can generate a higher 
                low_val = int(palindrome/999) # or //999 floor div gives int as answer 
                # highest possible factor to check, one factor must be lower than this
                high_val = int(palindrome**0.5) + 1 # **0.5 is "the square root" of palindrome 
                
                # check if palindrome divisible by any of the numbers between min and max
                for digit in range(low_val,high_val):
                    iterations += 1
                    if palindrome % digit == 0: #check for divisibility, since we are stepping through palindromes in order, as soon as we find one: we are Done! 
                       
                        return 'palindrome:', palindrome, 'digit:',digit, 'palindrome/digit:', palindrome/digit ,'iterations:',iterations #gives nicer close out of loops
    print({palindrome})                    


palindrome_create()