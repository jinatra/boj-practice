import sys

def check_sosu(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

ans = []
for n in range(M, N+1):
    if check_sosu(n) == True:
        ans.append(n)

if len(ans) == 0:
    print(-1)
else:
    print(sum(ans))
    print(ans[0])
