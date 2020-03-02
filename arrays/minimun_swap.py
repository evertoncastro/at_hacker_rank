#!/bin/python3


def minimumSwaps(arr):
    numSwaps = 0
    i = 0
    while(i < len(arr)-1):
        if arr[i] != i+1:
            tmp = arr[i]
            arr[i], arr[tmp-1] = arr[tmp-1], arr[i]
            numSwaps += 1
        else:
            i += 1
    return numSwaps


if __name__ == '__main__':

    arr = [9, 1, 2, 3, 4, 5, 8, 7, 6]

    result = minimumSwaps(arr)
    print(result)

# You are given an unordered array consisting of consecutive integers  [1, 2, 3, ..., n] without any duplicates. You are allowed to swap any two elements. You need to find the minimum number of swaps required to sort the array in ascending order.

# For example, given the array  we perform the following steps: