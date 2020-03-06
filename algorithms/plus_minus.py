import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    zeros = 0
    positives = 0
    negatives = 0
    for a in arr:
        if a == 0:
            zeros += 1
        elif a > 0:
            positives += 1
        else:
            negatives += 1
    print(round(positives/len(arr), 6))
    print(round(negatives/len(arr), 6))
    print(round(zeros/len(arr), 6))        


if __name__ == '__main__':
    n = 6
    arr = [-4, 3, -9, 0, 4, 1]
    plusMinus(arr)
