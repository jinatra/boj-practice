nums = []

for _ in range(10):
    nums.append(int(input()))

ans = set()
for i in nums:
    ans.add(i % 42)

print(len(ans))