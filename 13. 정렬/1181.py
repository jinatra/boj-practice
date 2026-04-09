import sys

N = int(sys.stdin.readline())

l = []
for _ in range(N):
    l.append(sys.stdin.readline().rstrip())

s = set(l)
s = sorted(s, key=lambda x: (len(x), x))
for i in s:
    print(i)