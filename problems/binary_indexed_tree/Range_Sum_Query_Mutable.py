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

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = [0] * len(nums)
        self.BIT = [0] * (len(nums) + 1)

        for i in range(len(nums)):
            self.updateTree(i, nums[i])

    def update(self, i: int, val: int) -> None:
        self.updateTree(i, val)

    def sumRange(self, i: int, j: int) -> int:
        return self.preSumTree(j) - self.preSumTree(i - 1)

    def updateTree(self, i, val):
        delta = val - self.nums[i]
        self.nums[i] = val

        i = i + 1
        while i < len(self.BIT):
            self.BIT[i] += delta
            i += self.lowbit(i)

    def preSumTree(self, i):
        res = 0
        i = i + 1
        while i > 0:
            res += self.BIT[i]
            i -= self.lowbit(i)
        return res

    def lowbit(self, x):
        return x & (-x)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
