import sys

N = int(sys.stdin.readline())

l = []
for _ in range(N):
    l.append(list(map(int, sys.stdin.readline().strip().split())))

l.sort(key=lambda x: (x[1], x[0]))

for [a,b] in l:
    print(a, b)