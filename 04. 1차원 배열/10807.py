import sys

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

ans = 0
for i in range(N):
    if l[i] == v:
        ans += 1
        
print(ans)