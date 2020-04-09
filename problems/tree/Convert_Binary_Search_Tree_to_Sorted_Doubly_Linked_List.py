'''
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
You can think of the left and right pointers as synonymous to the predecessor and successor
pointers in a doubly-linked list.

For a circular doubly linked list, the predecessor of the first element is the last element,
and the successor of the last element is the first element.

We want to do the transformation in place.
After the transformation, the left pointer of the tree node should point to its predecessor,
and the right pointer should point to its successor.
You should return the pointer to the smallest element of the linked list.

Constraints:
-1000 <= Node.val <= 1000
Node.left.val < Node.val < Node.right.val
All values of Node.val are unique.
0 <= Number of Nodes <= 2000
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return root

        preHead = Node()
        cur = preHead
        nxt = root
        stack = []
        while stack or nxt:
            while nxt:
                stack.append(nxt)
                nxt = nxt.left
            nxt = stack.pop()
            cur.right = nxt
            nxt.left = cur
            cur = nxt
            nxt = nxt.right

        cur.right = preHead.right
        preHead.right.left = cur
        return preHead.right
