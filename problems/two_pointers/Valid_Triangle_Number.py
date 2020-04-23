'''
https://leetcode.com/contest/leetcode-weekly-contest-36/problems/valid-triangle-number/

Given an array consists of non-negative integers, your task is to count the number of
triplets chosen from the array that can make triangles if we take them as side lengths
of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are:
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3

Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
'''

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for r in range(n - 1, 1, -1):
            i, j = 0, r - 1
            while i < j:
                if nums[i] + nums[j] <= nums[r]:
                    i += 1
                else:
                    res += j - i
                    j -= 1
        return res
                
