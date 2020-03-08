'''
https://leetcode.com/problems/range-sum-query-mutable/

Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j),
inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.
'''

class SegmentTreeNode:
    def __init__(self, start, end, val):
        self.start = start
        self.end = end
        self.left = self.right = None
        self.sum = val

class NumArray:
    def __init__(self, nums: List[int]):
        self.root = self.build(nums, 0, len(nums) - 1)

    def update(self, i: int, val: int) -> None:
        self.updateTree(self.root, i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.query(self.root, i, j)

    def build(self, nums, l, r):
        if l > r:
            return None

        root = SegmentTreeNode(l, r, nums[l])
        if l == r:
            return root

        mid = (l + r) // 2
        root.left = self.build(nums, l, mid)
        root.right = self.build(nums, mid + 1, r)
        root.sum = root.left.sum + root.right.sum
        return root

    def updateTree(self, root, i, val):
        if not root:
            return

        if root.start == root.end:
            if root.start == i:
                root.sum = val
            return

        mid = (root.start + root.end) // 2
        if i <= mid:
            self.updateTree(root.left, i, val)
        else:
            self.updateTree(root.right, i, val)
        root.sum = root.left.sum + root.right.sum

    def query(self, root, l, r):
        if r < root.start or l > root.end:
            return 0
        if l == root.start and r == root.end:
            return root.sum

        res = 0
        mid = (root.start + root.end) // 2
        if l <= mid:
            if r <= mid:
                leftSum = self.query(root.left, l, r)
            else:
                leftSum = self.query(root.left, l, mid)
            res += leftSum
        if r > mid:
            if l > mid:
                rightSum = self.query(root.right, l, r)
            else:
                rightSum = self.query(root.right, mid + 1, r)
            res += rightSum
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
