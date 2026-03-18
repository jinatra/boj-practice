import sys

N, M = map(int, sys.stdin.readline().split())

list = []
for i in range(N):
    list.append(i+1)

for m in range(M):
    i, j = map(int, sys.stdin.readline().split())
    rev = list[i-1:j]
    rev.reverse()
    list[i-1:j] = rev

print(' '.join(map(str, list)))