#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumDistances' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def minimumDistances(a):
    # Write your code here
    n = len(a)
    lst = [x for x in a if a.count(x) > 1]
    set1 = set(lst)
    lst = list(set1)
    print(lst)
    lst1 = []
    for i in lst:
        index1 = a.index(i)
        index2 = a.index(i,index1 + 1,n)
        lst1.append(abs(index1 - index2))
    if (len(lst1) == 0):
        return -1
    ans = min(lst1)
    return ans     

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
