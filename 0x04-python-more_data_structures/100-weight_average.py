#!/usr/bin/python3
def weight_average(my_list=[]):
    sum1, sum2 = 0, 0
    if my_list:
        for elm in my_list:
            sum1 += elm[0] * elm[1]
            sum2 += elm[1]
        return sum1/sum2
    return 0
