'''
https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/

Given an array nums and an integer target.

Return the maximum number of non-empty non-overlapping subarrays such that the sum of values
in each subarray is equal to target.

Example 1:
Input: nums = [1,1,1,1,1], target = 2
Output: 2
Explanation: There are 2 non-overlapping subarrays [1,1,1,1,1] with sum equals to target(2).

Example 2:
Input: nums = [-1,3,5,1,4,2,-9], target = 6
Output: 2
Explanation: There are 3 subarrays with sum equal to 6.
([5,1], [4,2], [3,5,1,4,2,-9]) but only the first 2 are non-overlapping.

Example 3:
Input: nums = [-2,6,6,3,5,4,1,2,8], target = 10
Output: 3

Example 4:
Input: nums = [0,0,0], target = 0
Output: 3

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
0 <= target <= 10^6
'''

from collections import defaultdict
class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        d = defaultdict(list)
        d[0].append(-1)
        presum = 0
        n = len(nums)
        f = [0] * (n + 1)
        for i, num in enumerate(nums):
            f[i + 1] = f[i]
            presum += num
            for j in d[presum - target]:
                f[i + 1] = max(f[i + 1], f[j + 1] + 1)
            d[presum].append(i)
        return f[n]
