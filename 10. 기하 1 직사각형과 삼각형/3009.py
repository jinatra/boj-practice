import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())
e, f = map(int, sys.stdin.readline().split())

x = [a, c, e]
y = [b, d, f]
dx = {}
dy = {}

for i in x:
    if i in dx:
        dx[i] += 1
    else:
        dx[i] = 1

for i in y:
    if i in dy:
        dy[i] += 1
    else:
        dy[i] = 1

ax = []
ay = []
for k, v in dx.items():
    if v == 1:
        ax.append(k)

for k,v  in dy.items():
    if v == 1:
        ay.append(k)

print(str(ax[0]) + ' ' + str(ay[0]))