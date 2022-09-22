#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number_str = str(number)
message1 = f'Last digit of {number} is {number_str[-1]}'
message2 = f'Last digit of {number} is -{number_str[-1]}'
if(number_str[0] == '-'):
    print(f"{message2} and is less than 6 and not 0")
else:
    if int(number_str[-1]) > 5:
        print(f"{message1} and is greater than 5")
    elif int(number_str[-1]) == 0:
        print(f"{message1} and is 0")
    else:
        print(f"{message1} and is less than 6 and not 0")
