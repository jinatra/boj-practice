import sys

N, M = map(int, sys.stdin.readline().split())

d = {}
for i in range(N):
    d[i+1] = i+1

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    val_i = d[j]
    val_j = d[i]
    d[i] = val_i
    d[j] = val_j

print(' '.join(map(str, d.values())))
