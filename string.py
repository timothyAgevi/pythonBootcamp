import random, string
letters_numbers = string.ascii_letters + string.digits
word = ''
word += random.choice(letters_numbers)
print(word)