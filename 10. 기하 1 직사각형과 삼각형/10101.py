import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())

sum = a + b + c
s = set([a, b, c])

if a == b == c == 60:
    print('Equilateral')
elif sum == 180 and len(s) == 2:
    print('Isosceles')
elif sum == 180 and len(s) == 3:
    print('Scalene')
else:
    print('Error')

