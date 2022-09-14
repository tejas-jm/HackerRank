#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    words = ["zero","one","two","three","four",
        "five","six","seven","eight","nine","ten",
        "eleven","twelve","thirteen","fourteen","fifteen",
        "sixteen","seventeen","eighteen","nineteen","twenty","twenty one","twenty two","twenty three","twenty four","twenty five","twenty six", "twenty seven","twenty eight","twenty nine","thirty"]
    if (m == 0):
        print(f"{words[h]} o' clock")
    if (1 <= m <= 30):
        if (m == 1):
            v = "one"
            print( f"{v} minute past {words[h]}")
        elif (m == 15):
            v = "quarter"
            print( f"{v} past {words[h]}")
        elif (m == 30):
            v = "half"
            print( f"{v} past {words[h]}")
        else:
            print( f"{words[m]} minutes past {words[h]}")
    if (31 <= m <= 59):
        if (m == 45):
            v = "ten"
            print( f"quarter to {words[h+1]}")
        else:
            print( f"{words[60 - m]} minutes to {words[h+1]}")

h = int(input().strip())

m = int(input().strip())

result = timeInWords(h, m)

