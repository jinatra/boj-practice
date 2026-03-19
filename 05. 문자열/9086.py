import sys

T = int(sys.stdin.readline())
for t in range(T):
    str = sys.stdin.readline()
    s1 = str[0]
    s2 = str.strip()[-1]
    print(s1+s2)