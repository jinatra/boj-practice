import sys

def find_sosu(n: int):
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

N = int(sys.stdin.readline())
li = list(map(int, sys.stdin.readline().split()))

ans = 0
for i in li:
    if i == 1:
        continue
    if find_sosu(i) == False:
        ans += 1

print(ans)

