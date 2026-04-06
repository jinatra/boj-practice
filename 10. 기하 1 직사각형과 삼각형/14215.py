import sys

a, b, c = map(int, sys.stdin.readline().split())

li = sorted([a, b, c], reverse=True)

if li[0] < li[1]+li[2]: # 그자체로 삼각형이 될 경우
    print(sum(li)) # 더하기
else: # 아닌 경우
    print((li[1]+li[2])*2 - 1)