#Sort Array By Parity II
#Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.You may return any answer array that satisfies this condition.
#Input: [4,2,5,7]
#Output: [4,5,2,7]
class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ev=[]
        od=[]
        r=[]
        for i in A:
            if i%2==0:
                ev.append(i)
            else:
                od.append(i)
        for i in range(0,len(ev)):
            r.append(ev.pop())
            r.append(od.pop())
        return r
        
