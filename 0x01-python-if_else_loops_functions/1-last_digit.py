#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
message = f'Last digit of {number} is -{number_str[-1]}'
if(number_str[0] == '-'):
    print(f"{message} and is less than 6 and not 0")
else:
    if int(number_str[-1]) > 5:
        print(f"{message} and is greater than 5")
    elif int(number_str[-1]) == 0:
        print(f"{message} and is 0")
    else:
        print(f"{message} and is less than 6 and not 0")
