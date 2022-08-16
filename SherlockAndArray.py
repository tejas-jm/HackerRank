#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def balancedSums(arr):
    # Write your code here
    #Brute Force Approach -> Time limit Exceeded
    # left = []
    # right = []
    # n = len(arr)
    # if n == 1:
    #     return "YES"
    # for i in range(n):
    #     right = arr[0:i:1]
    #     # print(right)
    #     left = arr[i+1:n:1]
    #     # print(left)
    #     if(sum(right) == sum(left)):
    #         return "YES"
    # return "NO"
    
    #Badass Approach
    
    tot = sum(arr)
    left = 0
    for i in arr:
        if left == tot - i - left :
            return "YES"
        left += i
    return "NO"
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
