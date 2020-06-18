#!/bin/python3
def miniMaxSum(arr):
    m = None
    h = None
    total = 0
    for a in arr:
        m = a if (m is None or a < m) else m
        h = a if (h is None or a > h) else h
        total += a

    return f'{total - h} {total - m}'


if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    print(miniMaxSum(arr))
