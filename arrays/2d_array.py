#!/bin/python3

def hourglassSum(arr):

    hour_glasses = []
    l_start = 0
    for l in range(len(arr)):
        if l >= 4:
            break
        while l_start <= 3:
            hour_glasses.append(sum(arr[l][l_start:l_start+3]) + arr[l+1][l_start+1] + sum(arr[l+2][l_start:l_start+3]))
            l_start += 1
        l_start = 0

    return max(hour_glasses)


if __name__ == '__main__':

    arr = [
        [1, 5, 5, 4, 1, 4],
        [1, 5, 5, 4, 1, 4],
        [1, 5, 5, 4, 1, 4],
        [1, 5, 5, 4, 1, 4],
        [1, 5, 5, 4, 1, 4],
        [1, 5, 5, 4, 1, 4]
    ]

    result = hourglassSum(arr)
    print(result)


