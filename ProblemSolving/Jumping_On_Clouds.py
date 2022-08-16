#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    n = len(c)
    jump = 0
    index = 0
    while (index < n - 2):
        if (c[index + 2] == 0 ):
            index = index + 2
            jump = jump + 1
        elif (c[index + 1] == 0):
            index = index + 1
            jump = jump + 1
        print(index)
    if (index < n - 1):
        jump = jump + 1 
    return jump


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
