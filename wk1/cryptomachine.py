def enigma_light():
# create keys string
    keys = 'abcdefghijklmnopqrstuvwxyz !'
# autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0:-1]
    # print(keys)
    # print(values)
# create two dictionaries
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values,keys)) 
# OR create 1 and then flip 
    dict_e = dict(zip(keys,values))
    dict_d = {value:key for key, value in dict_e.items()}
#user input 'the message' and mode
    msg = input('Enter your secret message quietly: ')
    mode = input('Crypto mode: encode (e) OR decode (d): ')
# run encode or decode
    if mode == 'e':
        new_msg = "".join[dict_e[letter] for letter in msg]
    elif mode == 'd':
        new_msg = "".join[dict_d[letter] for letter in msg]
    
    return new_msg
# return result
# clean and beautify the code 

print(enigma_light())