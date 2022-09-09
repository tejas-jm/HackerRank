#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jimOrders' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_INTEGER_ARRAY orders as parameter.
#

def jimOrders(orders):
    # Write your code here
    n = len(orders)
    lst = []
    for i in orders:
        lst.append(i[0] + i[1])
    lst1 = lst.copy()
    lst1.sort()
    print(lst1)
    print(lst)

    ans = []
    for j in lst1:
        print(lst.index(j))
        cust_id = lst.index(j) + 1 
        ans.append(cust_id)
        # print(lst)
    print(ans)
    print(orders)
    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    orders = []

    for _ in range(n):
        orders.append(list(map(int, input().rstrip().split())))

    result = jimOrders(orders)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
