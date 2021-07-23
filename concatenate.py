num =20
num2 = 10
sum = (num + num2) 
print(f'number is '  +  '' + str(num) + ' ' + 'and sum ' + ' ' + str(sum))

# contatenating integerg
# method 1 : use of str()
# method 2 : use of format
# method 3 : special use of format

# method 2 : use of format
print(f' number is' +' ' + format(num,'.2f') + ' '+ 'and sum',sum)

# method 3 : special use of format
s ='{:.2f},{}'.format(num,sum)
print(s)
Concatenate