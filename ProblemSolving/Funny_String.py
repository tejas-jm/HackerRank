#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'funnyString' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def funnyString(s):
    # Write your code here
    lst1 = [ord(x) for x in s]
    rev = s[::-1]
    lst2 = [ord(y) for y in rev]
    n = len(s)
    lst3 = []
    lst4 = []
    for i in range(n-1):
        value = abs(lst1[i] - lst1[i+1])
        lst3.append(value)
        value1 = abs(lst2[i] - lst2[i+1])
        lst4.append(value1)
    if (lst3 == lst4):
        return "Funny"
    return "Not Funny"
    
q = int(input().strip())

for q_itr in range(q):
    s = input()

    result = funnyString(s)
    print(result)

        

    
