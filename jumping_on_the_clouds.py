#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    jump = 0
    i = 0
    n = len(c)

    while i < (n - 1):
        if i + 2 >= n or c[i + 2] == 1:
            i += 1
            jump += 1
        else:
            i += 2
            jump += 1
    return jump

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #n = int(input())

    #c = list(map(int, input().rstrip().split()))
    #c = [0, 0, 0, 0, 1, 0]
    #c = [0, 0, 1, 0, 0, 1, 0]
    c = [0, 0, 0, 1, 0, 0]
    #c = [0, 0, 0, 1, 0]
    result = jumpingOnClouds(c)

    print(result)
