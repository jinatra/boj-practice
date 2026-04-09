import sys

N, M = map(int, sys.stdin.readline().split())
S = []
for _ in range(N):
    S.append(sys.stdin.readline())

S = set(S)

checks = []
for _ in range(M):
    checks.append(sys.stdin.readline())

ans = 0
for c in checks:
    if c in S:
        ans += 1

print(ans)

