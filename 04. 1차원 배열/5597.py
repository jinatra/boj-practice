submitted = set()

for _ in range(28):
    submitted.add(int(input()))

entire = set()
for i in range(30):
    entire.add(i+1)

ans = sorted(entire - submitted)

print(ans[0])
print(ans[1])
