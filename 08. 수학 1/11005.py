import sys

N, B = sys.stdin.readline().split()

d = {}
for i in range(10):
    d[str(i)] = i
for i in range(26):
    d[chr(65+i)] = 10+i

dic = {}
for k, v in d.items():
    dic[str(v)] = k

ans = ''
N, B = int(N), int(B)

while N > 0:
    n = N % B
    ans += dic[str(n)]
    N = N // B
ans = ans[::-1]
print(ans)