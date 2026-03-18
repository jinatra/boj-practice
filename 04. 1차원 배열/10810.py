import sys

N, M = map(int, sys.stdin.readline().split())

# N개의 바구니
# M번 공 넣음

d = {}
for i in range(N):
    d[i+1] = 0

# {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

for m in range(M):
    i, j, k = map(int, sys.stdin.readline().split())
    for iv in range(i, j+1):
        d[iv] = k

ans = []
for k, v in d.items():
    ans.append(str(v))

print(' '.join(ans))
