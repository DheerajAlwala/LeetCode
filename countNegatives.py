#Count Negative Numbers in a Sorted Matrix
#Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
#Output: 8
class Solution(object):
    def countNegatives(self, grid):
        c=0
        for ls in grid:
            for i in range(0,len(ls)):
                if ls[i]<0:
                    c+=1
        return c
                    
            
        
