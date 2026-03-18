import sys

N = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

max_val = max(l)
min_val = min(l)

print(f'{min_val} {max_val}')