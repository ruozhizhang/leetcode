'''
https://leetcode.com/problems/count-of-range-sum/

Given an integer array nums, return the number of range sums that lie in [lower, upper] inclusive. Range sum S(i, j) is defined as the sum of the elements in nums between indices i and j (i ≤ j), inclusive.

Note:
A naive algorithm of O(n^2) is trivial. You MUST do better than that.

Example:

Input: nums = [-2,5,-1], lower = -2, upper = 2,
Output: 3
Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective sums are: -2, -1, 2.
'''

class SegmentTreeNode:
    def __init__(self, min, max):
        self.min = min
        self.max = max
        self.left = None
        self.right = None
        self.cnt = 0

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        preSum = [0]
        for num in nums:
            preSum.append(preSum[-1] + num)

        preSumRange = sorted(set(preSum))
        root = self.build(preSumRange, 0, len(preSumRange) - 1)

        res = 0
        for p in preSum:
            res += self.count(root, p - upper, p - lower)
            self.update(root, p)
        return res

    def build(self, arr, l, r):
        if l > r:
            return None
            
        root = SegmentTreeNode(arr[l], arr[r])
        if l == r:
            return root

        mid = (l + r) // 2
        root.left = self.build(arr, l, mid)
        root.right = self.build(arr, mid + 1, r)
        return root

    def update(self, root, val):
        if not root:
            return
        if val < root.min or val > root.max:
            return

        root.cnt += 1
        self.update(root.left, val)
        self.update(root.right, val)

    def count(self, root, min, max):
        if not root:
            return 0
        if min > root.max or max < root.min:
            return 0
        if min <= root.min and max >= root.max:
            return root.cnt
        return self.count(root.left, min, max) + self.count(root.right, min, max)
