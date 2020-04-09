'''
https://leetcode.com/problems/subtree-of-another-tree/

Given two non-empty binary trees s and t, check whether tree t has exactly the same
structure and node values with a subtree of s.
A subtree of s is a tree consists of a node in s and all of this node's descendants.
The tree s could also be considered as a subtree of itself.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False

        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)


    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False

        return s.val == t.val and self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
