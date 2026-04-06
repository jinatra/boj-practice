import sys

N = int(sys.stdin.readline())
li = []
lx = []
ly = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    li.append([a, b])
    lx.append(a)
    ly.append(b)

xl = max(lx) - min(lx)
yl = max(ly) - min(ly)

print(xl*yl)