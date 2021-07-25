#  find largest palindrom between 10 and 20
import time
def is_palindrome(val):
    val = str(val)
     # convert the value to string
    return str(val) == str(val)[::-1]
   

def palindrome():
    start_time = time.time
    palindrom_list = []
    debug_list = []
    iterations = 0
    lowNum = 10
    highNum = 20

    for num1 in range(lowNum,highNum):
        for num2 in range(lowNum,highNum):
            iterations +=1
            if is_palindrome(num1*num2):
                palindrom_list.append(num1*num2)# append takes only 1 argument
                debug_list.append([num1,num2,palindrom_list])
                print(palindrom_list)
                # print(debug_list)
                print('Largest palindrome:', max(palindromes_list))
palindrome()                


        

