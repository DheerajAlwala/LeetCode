#283. Move Zeroes
class Solution(object):
    def moveZeroes(self, nums):
        czero=nums.count(0)
        while 0 in nums:
            nums.remove(0)
        for i in range(czero):
            nums.append(0)
    
        
