#!/bin/python3


def diagonalDifference(arr):
    index = 1
    final = 0

    for li in arr:
        final += li[-1 + index] - li[len(arr) - index]
        index += 1

    return abs(final)


if __name__ == '__main__':
    n = 9
    arr = []
    arr.append([11, 2, 4])
    arr.append([4, 5, 6])
    arr.append([10, 8, -12])
    result = diagonalDifference(arr)
    print(result)
