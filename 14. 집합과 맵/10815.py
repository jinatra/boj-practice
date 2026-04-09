import sys

N = int(sys.stdin.readline())
num_cards = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().rstrip().split()))

num_set = set(num_cards)
ans = []
for n in nums:
    if n in num_set:
        ans.append('1')
    else:
        ans.append('0')

print(' '.join(ans))