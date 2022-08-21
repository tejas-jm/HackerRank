#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kaprekarNumbers' function below.
#
# The function accepts following parameters:
#  1. INTEGER p
#  2. INTEGER q
#

def kaprekarNumbers(p, q):
    # Write your code here
    count = 0
    for i in range(p,q+1):
        num_str = str(i)
        n = len(num_str)
        square = pow(i,2)
        square_str = str(square)
        m = len(square_str)
        right_substring = square_str[m-n:]
        left_substring = square_str[0:m-n]
        right = int(right_substring)
        try:
          left = int(left_substring)
        except:
            left = 0
        if (left + right == i):
            print(i, end =" ")
            count += 1
    # print(count)
    if (count == 0):
        print("INVALID RANGE")
        

if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
