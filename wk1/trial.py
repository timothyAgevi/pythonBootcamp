

def trial():
    low_val = 1
    high_val = 3
    iterations = 0
    numbers = []
    low_val2 = 1
    for num1 in range(high_val,low_val, -1):
        for num2 in range(high_val,low_val, -1):
            iterations +=1
            numbers.append([num1,num2])
            if num1 == num2:
                continue
            print(iterations)
            print(numbers)
                
                
trial()
# output
1
[[3, 3]]
2
[[3, 3], [3, 2]]
3
[[3, 3], [3, 2], [2, 3]]
4
[[3, 3], [3, 2], [2, 3], [2, 2]]

#  if include : low_val2 = 1
# just same as above
1
[[3, 3]]
2
[[3, 3], [3, 2]]
3
[[3, 3], [3, 2], [2, 3]]
4
[[3, 3], [3, 2], [2, 3], [2, 2]]

# if include : num1 ==num2:break
2
[[3, 3], [2, 3]]

# if include : num1 ==num2:continue
2
[[3, 3], [3, 2]]
3
[[3, 3], [3, 2], [2, 3]