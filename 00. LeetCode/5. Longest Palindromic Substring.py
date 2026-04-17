class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            # 가운데가 홀수
            odd = self.expand(s, i, i)
            # 가운데가 짝수
            even = self.expand(s, i, i+1)
        
            # 제일 긴거 체크
            if len(odd) > len(ans):
                ans = odd
            if len(even) > len(ans):
                ans = even
        
        return ans

    # 양옆으로 어디까지 확장가능한지
    def expand(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left+1:right]