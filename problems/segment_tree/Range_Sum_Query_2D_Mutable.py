'''
https://leetcode.com/problems/range-sum-query-2d-mutable/

Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper
left corner (row1, col1) and lower right corner (row2, col2).


Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10
Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.
'''

class SegmentTreeNode:
    def __init__(self, start, end, sum):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.sum = sum

class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            return
        self.m, self.n = len(matrix), len(matrix[0])
        self.root = self.build(matrix, 0, self.m * self.n - 1)

    def update(self, row: int, col: int, val: int) -> None:
        index = row * self.n + col
        self.updateTree(self.root, index, val)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        for i in range(row1, row2 + 1):
            start = i * self.n + col1
            end = i * self.n + col2
            res += self.queryTree(self.root, start, end)
        return res

    def build(self, A, start, end):
        if start > end:
            return None

        x, y = divmod(start, self.n)
        root = SegmentTreeNode(start, end, A[x][y])
        if start == end:
            return root

        mid = (start + end) // 2
        root.left = self.build(A, start, mid)
        root.right = self.build(A, mid + 1, end)
        root.sum = root.left.sum + root.right.sum
        return root

    def updateTree(self, root, index, val):
        if not root:
            return

        if root.start == root.end:
            if root.start == index:
                root.sum = val
            return

        mid = (root.start + root.end) // 2
        if index <= mid:
            self.updateTree(root.left, index, val)
        else:
            self.updateTree(root.right, index, val)
        root.sum = root.left.sum + root.right.sum

    def queryTree(self, root, start, end):
        if not root:
            return 0
        if start > root.end or end < root.start:
            return 0
        if start <= root.start and end >= root.end:
            return root.sum

        mid = (root.start + root.end) // 2
        res = 0
        if start <= mid:
            if end <= mid:
                lSum = self.queryTree(root.left, start, end)
            else:
                lSum = self.queryTree(root.left, start, mid)
            res += lSum
        if end > mid:
            if start > mid:
                rSum = self.queryTree(root.right, start, end)
            else:
                rSum = self.queryTree(root.right, mid + 1, end)
            res += rSum
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# obj.update(row,col,val)
# param_2 = obj.sumRegion(row1,col1,row2,col2)
