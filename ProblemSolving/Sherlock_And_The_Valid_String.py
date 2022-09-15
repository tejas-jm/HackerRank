#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isValid(s):
 
    lst = list(Counter(list(Counter(s).values())).values())
    if len(lst) == 1:
        return "YES"
    elif len(lst) > 2:
        return "NO"
    elif len(lst) == 2:
       c =  lst.pop()
       if c > 1:
        return "NO"
       else:
        return "YES"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input().strip()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
