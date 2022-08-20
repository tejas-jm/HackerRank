#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cutTheSticks' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def cutTheSticks(arr):
    # Write your code here
    n = 1
    while (n > 0):
        lst = arr
        # print(lst[0])
        print(len(arr))
        lst.sort()
        cut = lst[0]
        arr = [x - cut for x in arr]
        arr = list(filter((0).__ne__,arr))
        n = len(arr)

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = cutTheSticks(arr)

