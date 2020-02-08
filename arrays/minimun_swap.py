#!/bin/python3


def minimumSwaps(arr):
    swap = 0
    i = 0
    while i < len(arr):
        dif = 0
        if i+1 > len(arr)-1:
            pass
        elif arr[i] > arr[i+1]:
            dif += 1
            if i + 2 > len(arr) - 1:
                pass
            elif arr[i] > arr[i+2]:
                if i + 3 > len(arr) - 1:
                    pass
                elif arr[i] > arr[i+3]:
                    dif += 1
        if dif > 0:
            cur = arr[i]
            arr[i] = arr[i+dif]
            arr[i+dif] = cur
            swap += 1
            i = 0
            continue
        i += 1
        continue
    print(arr)
    return swap


if __name__ == '__main__':

    arr = [9, 1, 2, 3, 4, 5, 8, 7, 6]

    result = minimumSwaps(arr)
    print(result)

