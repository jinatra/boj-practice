import sys

while True:
    nums = sorted(list(map(int, sys.stdin.readline().split())), reverse = True)
    if sum(nums) == 0:
        break
    s = set(nums)
    if nums[0] >= nums[1] + nums[2]:
        print('Invalid')
    elif len(s) == 1:
        print('Equilateral')
    elif len(s) == 2:
        print('Isosceles ')
    else:
        print('Scalene')