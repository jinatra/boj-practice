import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

ans = []
for i in range(N):
    if A[i] < X:
        ans.append(A[i])

print(' '.join(map(str, ans)))