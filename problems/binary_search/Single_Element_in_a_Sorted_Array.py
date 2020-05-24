'''
https://leetcode.com/problems/single-element-in-a-sorted-array/

You are given a sorted array consisting of only integers where every element appears
exactly twice, except for one element which appears exactly once. Find this single
element that appears only once.

Example 1:
Input: [1,1,2,3,3,4,4,8,8]
Output: 2

Example 2:
Input: [3,3,7,7,10,11,11]
Output: 10

Note: Your solution should run in O(log n) time and O(1) space.
'''

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l + 1 < r:
            mid = l + (r - l) // 2
            if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
                return nums[mid]
            elif nums[mid] == nums[mid - 1]:
                if (mid - l) % 2 == 0:
                    r = mid
                else:
                    l = mid + 1
            else:
                if (mid - l) % 2 == 0:
                    l = mid
                else:
                    r = mid - 1
        if l == 0 or nums[l] != nums[l - 1]:
            return nums[l]
        return nums[r]
