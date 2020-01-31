#!/bin/python3


def countingValleys(n, s):
    v = 0
    hiker = 0
    for step in s:
        if step == 'U':
            hiker += 1
            direction = 'up'
        else:
            hiker -= 1
            direction = 'down'

        if hiker == 0 and direction == 'up':
            v += 1
    return v

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = 'UDDDUDUU'
    n = 8
    result = countingValleys(n, s)
    print(result)
