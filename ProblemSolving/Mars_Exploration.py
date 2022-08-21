#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def marsExploration(s):
    # Write your code here
    n = len(s)
    msg = "SOS"
    times = int(n/3)
#     print(times)
    real_msg = ""
    real_msg =  msg*times
#     print(real_msg)
    changes = 0
    for i in range(n):
        if (s[i] != real_msg[i]):
            changes += 1
    return changes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()
