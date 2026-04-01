import sys

while True:
    n = int(sys.stdin.readline())
    if n == -1:
        break
    yl = []
    for i in range(1, n):
        if n % i == 0:
            yl.append(i)
    if sum(yl) == n:
        print(str(n) + ' = '  + ' + '.join(map(str, yl)))
    else:
        print(f'{n} is NOT perfect.')