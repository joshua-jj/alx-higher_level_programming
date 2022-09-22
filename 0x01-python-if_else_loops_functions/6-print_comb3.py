for i in range(10):
    for j in range(10):
        if i < j:
            if i != 8:
                print('{}'.format(i), end='')
                print('{}'.format(j), end=', ')
        else:
            continue
print(89)

