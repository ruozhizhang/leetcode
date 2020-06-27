'''
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and
conquer approach, which is more subtle.
'''

# Approach 1: DP, O(n) time, O(n) space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 1)
        res = float('-inf')
        for i in range(1, n + 1):
            f[i] = nums[i - 1] + (f[i - 1] if f[i - 1] > 0 else 0)
            res = max(res, f[i])
        return res

# Approach 2: prefix sum, O(n) time, O(1) space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        preSum = minPre = 0
        res = float('-inf')
        for num in nums:
            preSum += num
            res = max(res, preSum - minPre)
            minPre = min(minPre, preSum)
        return res
