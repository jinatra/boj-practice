import sys

S  = input()
alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ]

ans = ''
for a in alp:
    if a in S:
        ans += f'{S.index(a)} '
    else:
        ans += '-1 '
        
print(ans.strip())