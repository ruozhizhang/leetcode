'''
https://leetcode.com/problems/constrained-subset-sum/

Given an integer array nums and an integer k, return the maximum sum of a non-empty
subset of that array such that for every two consecutive integers in the subset,
nums[i] and nums[j], where i < j, the condition j - i <= k is satisfied.

A subset of an array is obtained by deleting some number of elements (can be zero)
from the array, leaving the remaining elements in their original order.

Example 1:
Input: nums = [10,2,-10,5,20], k = 2
Output: 37
Explanation: The subset is [10, 2, 5, 20].

Example 2:
Input: nums = [-1,-2,-3], k = 1
Output: -1
Explanation: The subset must be non-empty, so we choose the largest number.

Example 3:
Input: nums = [10,-2,-10,-5,20], k = 2
Output: 23
Explanation: The subset is [10, -2, -5, 20].

Constraints:
1 <= k <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
'''

'''
Algorithm: similar idea to Sliding Window Maximum
'''

from collections import deque
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        res = float('-inf')
        q = deque()
        for i in range(len(nums) - 1, -1, -1):
            cur = nums[i]
            while q and q[0][0] > i + k:
                q.popleft()
            if q and q[0][1] > 0:
                cur += q[0][1]
            while q and q[-1][1] <= cur:
                q.pop()
            q.append((i, cur))
            res = max(res, cur)
        return res
