class Solution:
    def reverse(self, x: int) -> int:
        max = 2**31
        if x >= 0:
            ans = int(str(x)[::-1])
            if -max <= ans <= max - 1:
                return ans
            else:
                return 0
        else: # 음수
            x *= -1
            ans = -1 * int(str(x)[::-1])
            if -max <= ans <= max - 1:
                return ans
            else:
                return 0