import sys

N = int(sys.stdin.readline())

l = list((map(int, sys.stdin.readline().rstrip().split())))
jrl = list(set(l))
jrl.sort()

d = {}
for i in range(len(jrl)):
    d[jrl[i]] = i

ans = []
for i in l:
    ans.append(str(d[i]))

print(' '.join(ans))
