#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    binary = bin(n).replace("0b","")
    lst = list(binary)
    count = 0
    result = 0
    n = len(lst)
    # print(lst)
    for i in range(0,n):
        
        if (int(lst[i]) == 0):
            count = 0
        else:
            count += 1
            result = max(result,count)
    print(result)
