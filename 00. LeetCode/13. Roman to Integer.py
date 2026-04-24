class Solution:
    def romanToInt(self, s: str) -> int:
        syms = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
        vals = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
        
        ans = 0
        while len(s) > 0:
            two = s[0:2]
            if two in syms:
                ind = syms.index(two)
                ans += vals[ind]
                s = s[2:]
            else:
                char = two[0]
                ind = syms.index(char)
                ans += vals[ind]
                s = s[1:]
        return ans