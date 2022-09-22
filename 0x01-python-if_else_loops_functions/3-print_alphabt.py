#!/usr/bin/python3
for i in range(97, 123):
    char = chr(i)
    if char == 'q' or char == 'e':
        continue
    else:
        print('{}'.format(char), end='')
