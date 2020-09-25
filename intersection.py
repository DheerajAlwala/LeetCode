#Intersection of Two Arrays
#Given two arrays, write a function to compute their intersection.
#Input: nums1 = [1,2,2,1], nums2 = [2,2]
#Output: [2]
class Solution(object):
    def intersection(self, nums1, nums2):
        s1=set(nums1)
        s2=set(nums2)
        i=s1.intersection(s2)
        return list(i)
        
