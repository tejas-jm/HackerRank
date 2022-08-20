#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    binary = '{:032b}'.format(n)
    # print(binary)
    lst = [int(x) for x in binary]
    # print(lst)
    n = len(lst)
    for i in range(n):
        if(lst[i] == 1):
           lst[i] = 0
        elif (lst[i] == 0):
            lst[i] = 1
    # print(lst)
    lst = [str(x) for x in lst]
    str1 = "".join(lst)
    # print(str1)
    flipped_num = int(str1,2)
    return flipped_num
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
