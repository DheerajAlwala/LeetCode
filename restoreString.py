#Shuffle String
#Given a string s and an integer array indices of the same length.The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
#Input: s = "abc", indices = [0,1,2]
#Output: "abc"
class Solution(object):
    def restoreString(self, s, indices):
        restored = [""] * len(s)
        for i in indices:
            restored[indices[i]] = s[i]
        return "".join(restored)
