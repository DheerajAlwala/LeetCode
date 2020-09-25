#Intersection of Two Arrays II
#Given two arrays, write a function to compute their intersection.
#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2,2]
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ls=[]
        for i in nums1:
            if i in nums2:
                ls.append(i)
                nums2.remove(i)
        return ls
                
                
        
