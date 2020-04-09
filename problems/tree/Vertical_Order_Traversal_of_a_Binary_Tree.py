'''
https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

Given a binary tree, return the vertical order traversal of its nodes values.
For each node at position (X, Y), its left and right children respectively
will be at positions (X-1, Y-1) and (X+1, Y-1).

Running a vertical line from X = -infinity to X = +infinity, whenever the
vertical line touches some nodes, we report the values of the nodes in order
from top to bottom (decreasing Y coordinates).

If two nodes have the same position, then the value of the node that is reported
first is the value that is smaller.

Return an list of non-empty reports in order of X coordinate.
Every report will have a list of values of nodes.

Note:
The tree will have between 1 and 1000 nodes.
Each node's value will be between 0 and 1000.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = defaultdict(list)
        s = [(root, 0, 0)]
        minX, maxX = float('inf'), float('-inf')
        while s:
            cur, i, j = s.pop()
            d[i].append((-j, cur.val))
            minX, maxX = min(minX, i), max(maxX, i)
            if cur.right:
                s.append((cur.right, i + 1, j - 1))
            if cur.left:
                s.append((cur.left, i - 1, j - 1))

        res = []
        for i in range(minX, maxX + 1):
            res.append([a[1] for a in sorted(d[i])])
        return res
