class Solution:
    def myAtoi(self, s: str) -> int:
        # STEP 1
        s = s.strip()
        
        if not s:
            return 0
        
        # STEP 2
        sign = 0
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            sign = 1
            s = s[1:]
        elif s[0].isdigit():
            sign = 1
        else:
            return 0
        
        # STEP 3
        num = ''
        for i in s:
            if i.isdigit():
                num += i
            else:
                break
        
        if not num:
            return 0
        
        # STEP 4
        max = 2**31
        n = int(num) * sign
        if n < -max:
            return -max
        elif n > max-1:
            return max-1
        else:
            return n