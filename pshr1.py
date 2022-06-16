#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

#[11 2 4 4 5 6 10 8 -12]
def diagonalDifference(arr):
    l=len(arr)
    ls,rs=0,0
    for i in range(l):
        for j in range(l):
            if i==j:
                ls+=arr[i][j]
            if (i+j)==(l-1):
                rs+=arr[i][j]
    return (abs(ls-rs))

if __name__ == '__main__':
    n = int(input().strip())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
