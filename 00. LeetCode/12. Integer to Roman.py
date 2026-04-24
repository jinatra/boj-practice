class Solution:
    def intToRoman(self, num: int) -> str:
        l = len(str(num))
        if l == 4:
            a = self.thousand(int(str(num)[0]) * 1000)
            b = self.hundred(int(str(num)[1]) * 100)
            c = self.ten(int(str(num)[2]) * 10)
            d = self.one(int(str(num)[3]) * 1)
            return a+b+c+d
        elif l == 3:
            b = self.hundred(int(str(num)[0]) * 100)
            c = self.ten(int(str(num)[1]) * 10)
            d = self.one(int(str(num)[2]) * 1)
            return b+c+d
        elif l == 2:
            c = self.ten(int(str(num)[0]) * 10)
            d = self.one(int(str(num)[1]) * 1)
            return c+d
        else:
            return self.one(num)

    def one(self, num: int):
        if num == 4:
            return 'IV'
        
        if num == 9:
            return 'IX'
        
        if num < 5:
            return 'I' * num
        else:
            return ('V' + (num - 5)*'I')
    
    def ten(self, num: int):
        if num == 40:
            return 'XL'
        
        if num == 90:
            return 'XC'
        
        if num < 50:
            return ('X' * (num // 10))
        else:
            return ('L' + ((num - 50) // 10) * 'X')
    
    def hundred(self, num: int):
        if num == 400:
            return 'CD'
        
        if num == 900:
            return 'CM'
        
        if num < 500:
            return ('C' * (num // 100))
        else:
            return ('D' + ((num - 500) // 100) * 'C')
    
    def thousand(self, num: int):
        return ((num // 1000) * 'M')

class Solution2:
    def intToRoman(self, num: int) -> str:
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        
        result = ''
        for i in range(len(values)):
            while num >= values[i]:
                result += symbols[i]
                num -= values[i]
        
        return result