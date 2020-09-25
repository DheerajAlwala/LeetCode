#Valid Anagram
#Given two strings s and t , write a function to determine if t is an anagram of s.
#Input: s = "anagram", t = "nagaram"
#Output: true
class Solution(object):
    def isAnagram(self, s, t):
        b=False
        if len(s)!=len(t):
            return False;
        else:
            ls1=[i for i in s]
            ls2=[i for i in t]
            ls1.sort()
            ls2.sort()
            if ls1==ls2:
                b=True
        return b
            
        
