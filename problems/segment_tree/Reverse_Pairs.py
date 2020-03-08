'''
https://leetcode.com/problems/reverse-pairs/

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.
'''

class SegmentTreeNode:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None
        self.cnt = 0

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        sortedNums = sorted(set(nums))

        root = self.build(sortedNums, 0, len(sortedNums) - 1)

        res = 0
        for i in range(len(nums) - 1, -1, -1):
            maxAllowed = nums[i] // 2 if nums[i] & 0x1 else nums[i] // 2 - 1
            res += self.query(root, float('-inf'), maxAllowed)
            self.update(root, nums[i])
        return res

    def build(self, nums, start, end):
        if start > end:
            return None

        root = SegmentTreeNode(nums[start], nums[end])
        if start == end:
            return root

        mid = (start + end) // 2
        root.left = self.build(nums, start, mid)
        root.right = self.build(nums, mid + 1, end)
        return root

    def query(self, root, start, end):
        if not root:
            return 0
        if start <= root.start and end >= root.end:
            return root.cnt
        if start > root.end or end < root.start:
            return 0

        return self.query(root.left, start, end) + self.query(root.right, start, end)

    def update(self, root, val):
        if not root:
            return

        if root.start <= val <= root.end:
            root.cnt += 1
            self.update(root.left, val)
            self.update(root.right, val)
