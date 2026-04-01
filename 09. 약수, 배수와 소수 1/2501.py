import sys

N, K = map(int, sys.stdin.readline().split())

yl = []

for n in range(1, N+1):
    if N % n == 0:
        yl.append(n)

if len(yl) < K:
    print(0)
else:
    print(yl[K-1])