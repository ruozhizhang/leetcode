'''
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/

Given an array of integers nums and a positive integer k, find whether it's possible
to divide this array into k non-empty subsets whose sums are all equal.


Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with
equal sums.

Note:
1 <= k <= len(nums) <= 16.
0 < nums[i] < 10000.
'''

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if len(nums) < k:
            return False
        total = sum(nums)
        if total % k != 0:
            return False
        targetSum = total // k
        nums.sort(reverse=True)
        return self.helper(nums, k, 0, targetSum, 0, {})

    def helper(self, nums, k, mask, targetSum, curSum, cache):
        if (mask, k) in cache:
            return cache[(mask, k)]
        if k == 0:
            return True

        res = False
        for i in range(len(nums)):
            if mask & (1 << i) == 0:
                if curSum + nums[i] == targetSum:
                    res = res or self.helper(nums, k - 1, mask | (1 << i), targetSum, 0, cache)
                elif curSum + nums[i] < targetSum:
                    res = res or self.helper(nums, k, mask | (1 << i), targetSum, curSum + nums[i], cache)

        cache[(mask, k)] = res
        return res
