#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximizingXor function below.
def maximizingXor(l, r):
    diff = r-l
    dict = {}
    for i in range(diff+1):
        j = 0
        while j <= i:
            xor = (l + i) ^ (l + j)
            dict['('+str(l + j)+')('+str(l + i)+")"] = xor
            j += 1
    return dict[max(dict, key=dict.get)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input())

    r = int(input())

    result = maximizingXor(l, r)

    fptr.write(str(result) + '\n')

    fptr.close()