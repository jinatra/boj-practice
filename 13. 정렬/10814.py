import sys

N = int(sys.stdin.readline())

l = []
i = 0
for _ in range(N):
    info = list(sys.stdin.readline().rstrip().split())
    info.append(i)
    l.append(info)
    i += 1

l.sort(key=lambda x: (int(x[0]), x[2]))

for [a, b, _] in l:
    print(a, b)