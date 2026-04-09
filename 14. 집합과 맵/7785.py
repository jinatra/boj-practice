import sys

n = int(sys.stdin.readline())

d = {}
for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    d[a]= b

ans = []
for k, v in d.items():
    if v == 'enter':
        ans.append(k)

ans.sort(reverse=True)
for a in ans:
    print(a)