import sys

N, B = sys.stdin.readline().split()

dic = {}
for i in range(10):
    dic[str(i)] = i
for i in range(26):
    dic[chr(65+i)] = 10 + i

N = N[::-1]

ans = 0
for i in range(len(N)):
    ans += dic[N[i]] * (int(B)**i)

print(ans)

