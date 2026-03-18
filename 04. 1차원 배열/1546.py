import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))

ms = max(scores)
new_scores = []

for s in scores:
    new_scores.append(s/ms * 100)

print(round(sum(new_scores)/N, 2))