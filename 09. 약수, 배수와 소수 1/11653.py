import sys

N = int(sys.stdin.readline())

n = 2
nam = 0

while N != 1:
    if N % n == 0:
        N = N // n
        print(n)
    else:
        n += 1