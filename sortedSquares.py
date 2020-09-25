#Squares of a Sorted Array
#Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.
#Input: [-4,-1,0,3,10]
#Output: [0,1,9,16,100]
 class Solution(object):
    def sortedSquares(self, A):
        for i in range(0,len(A)):
            A[i]**=2
        A.sort()
        return A
        
