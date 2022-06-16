#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    l,p,n,z=len(arr),0,0,0
    for i in arr:
        if i>0:
            p+=1
        elif i<0:
            n+=1
        else:
            z+=1
    if z==0:
        print('%.6f'%round(p/l,6),'%.6f'%round(n/l,6),"0.000000",sep="\n")
    else:
        print('%.6f'%round(p/l,6),'%.6f'%round(n/l,6),'%.6f'%round(z/l,6),sep="\n")

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
