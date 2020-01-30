#!/bin/python3


def repeatedString(s, n):
    return s[:n % len(s)].count('a') + s.count('a') * (n // len(s))

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = 'aba'
    n = 10
    result = repeatedString(s, n)

    print(result)
