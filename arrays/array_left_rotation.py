#!/bin/python3


def rotLeft(a, d):
    d = d % len(a)
    new_a = []
    i = 0
    while len(new_a) != len(a):
        new_a.append(str(a[i + d]))
        i += (-i - d) if i >= (len(a) - d - 1) else 1
    return new_a


if __name__ == '__main__':

    arr = [1, 2, 3, 4, 5]

    result = rotLeft(arr, 63)
    print(result)


