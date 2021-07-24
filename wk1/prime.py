# prime numbers between 1 and 10
#note in range(a,b) doesnt include b
# prime mumber: positive number with only 2 divisors(1 and itself)
# 1 is not a prime number
print([ x for x in range(2,11)
  if not any ([x % y == 0 for y in range(2,x)])])

# print([x for x in range(2, 151) 
# if not any([x % y == 0 for y in range(2, x)])])
  