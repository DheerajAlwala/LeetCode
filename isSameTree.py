# 100. Same Tree
#Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checker(self, t1, t2):
        if(t1 is not None and t2 is not None):
            if(t1.val == t2.val):
                return self.checker(t1.left, t2.left) and self.checker(t1.right, t2.right)
            return False
        if(t1 is None and t2 is None):
            return True
        else:
            return False

    def isSameTree(self, t1: TreeNode, t2: TreeNode) -> bool:
        if(t1 is None and t2 is None):
            return True
        return self.checker(t1, t2)
        
