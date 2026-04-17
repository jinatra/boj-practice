class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        rows = ['' for _ in range(numRows)]
        row = 0
        count = 1
        for i in range(len(s)):
            rows[row] += s[i]
            row += count
            if row == 0 or row == numRows - 1:
                count *= -1
        return ''.join(rows)