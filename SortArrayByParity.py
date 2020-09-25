#Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#Input: [3,1,2,4]
#Output: [2,4,3,1]
#The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

You may return any answer array that satisfies this condition.
class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ev=[]
        od=[]
        for i in A:
            if i%2==0:
                ev.append(i)
            else:
                od.append(i)
        ev.extend(od)
        return ev
