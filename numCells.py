#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numCells' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY grid as parameter.
#

def numCells(grid):
    c = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            arr, t = [], 0
            if i-1 >= 0 and j-1 >= 0:
                arr.append(grid[i-1][j-1])
            if i-1 >= 0:
                arr.append(grid[i-1][j])
            if i-1 >= 0 and j+1 < len(grid[0]):
                arr.append(grid[i-1][j+1])
            if j-1 >= 0:
                arr.append(grid[i][j-1])
            if j+1 < len(grid[0]):
                arr.append(grid[i][j+1])
            if i+1 < len(grid) and j-1 >= 0:
                arr.append(grid[i+1][j-1])
            if i+1 < len(grid):
                arr.append(grid[i+1][j])
            if i+1 < len(grid) and j+1 < len(grid[0]):
                arr.append(grid[i+1][j+1])
            #print(arr)
            for k in range(len(arr)):
                if arr[k] < grid[i][j]:
                    t += 1
            if t == len(arr):
                c += 1
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grid_rows = int(input().strip())
    grid_columns = int(input().strip())

    grid = []

    for _ in range(grid_rows):
        grid.append(list(map(int, input().rstrip().split())))

    result = numCells(grid)

    fptr.write(str(result) + '\n')

    fptr.close()
