#########################PASSWORD STRENGTH CHECKER########################
import re
print("Password Strength checker")
v=input("Enter the password:")
if(len(v)>=8):
    if(bool(re.match('((?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#$%^&*]).{8,30})',v))==True):
        print("The password is strong")
    elif(bool(re.match('((\d*)([a-z]*)([A-Z]*)([!@#$%^&*]*).{8,30})',v))==True):
        print("The password is weak")
else:
    print("You have entered an invalid password.")
    
    
    
    
    
    
    ####################   PASSWORD GENERATOR  #####################
import random

import string

print('Welcome to Password generator!')

length = int(input('\nEnter the length of password: '))

lower = string.ascii_lowercase

upper = string.ascii_uppercase

num = string.digits

symbols = string.punctuation

all = lower + upper + num + symbols

temp = random.sample(all, length)

password = "".join(temp)

print(password)

