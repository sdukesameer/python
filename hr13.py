import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    o='';t=0
    try:
        s=s[0].upper()+s[1:]
    except:
        pass
    for i in s:
        if i==' ':
            t=1
            o+=i
            continue
        if t==1:
            o+=i.upper()
            t=0
            continue
        o+=i
    return o


if __name__ == '__main__':
    s = input()
    result = solve(s)
    print(result)
