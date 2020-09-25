#172. Factorial Trailing Zeroes
class Solution(object):
    def trailingZeroes(self, n):
        c = 0
        i=5
        while (n/i>=1): 
            c += int(n/i) 
            i *= 5
        return c
            
            
        
