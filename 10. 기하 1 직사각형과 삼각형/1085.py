import sys

x, y, w, h = map(int, sys.stdin.readline().rstrip().split())

l = []
l.append(x)
l.append(y)
l.append(abs(x-w))
l.append(abs(y-h))

print(min(l))