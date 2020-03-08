'''
https://leetcode.com/problems/count-of-smaller-numbers-after-self/

You are given an integer array nums and you have to return a new counts array. The counts array
has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
'''

class SegmentTreeNode:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.left = None
        self.right = None
        self.cnt = 0

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sortedNums = sorted(set(nums))

        root = self.build(sortedNums, 0, len(sortedNums) - 1)

        res = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            res[i] = self.query(root, float('-inf'), nums[i] - 1)
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

    def update(self, root, num):
        if not root:
            return

        if root.low <= num <= root.high:
            root.cnt += 1
            self.update(root.left, num)
            self.update(root.right, num)

    def query(self, root, low, high):
        if not root:
            return 0
        if low > root.high or high < root.low:
            return 0
        if low <= root.low and high >= root.high:
            return root.cnt

        return self.query(root.left, low, high) + self.query(root.right, low, high)
