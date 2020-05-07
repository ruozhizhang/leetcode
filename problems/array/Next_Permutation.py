'''
https://leetcode.com/problems/next-permutation/

Implement next permutation, which rearranges numbers into the lexicographically
next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible
order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding
outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        start = -1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                start = i - 1
                break
        if start == -1:
            nums.reverse()
            return

        for i in range(len(nums) - 1, start, -1):
            if nums[i] > nums[start]:
                end = i
                break
        nums[start], nums[end] = nums[end], nums[start]
        l, r = start + 1, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
