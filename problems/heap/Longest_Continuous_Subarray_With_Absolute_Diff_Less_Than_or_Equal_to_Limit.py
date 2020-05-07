'''
https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

Given an array of integers nums and an integer limit, return the size of the longest
continuous subarray such that the absolute difference between any two elements is
less than or equal to limit.

In case there is no subarray satisfying the given condition return 0.

Example 1:
Input: nums = [8,2,4,7], limit = 4
Output: 2
Explanation: All subarrays are:
[8] with maximum absolute diff |8-8| = 0 <= 4.
[8,2] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4] with maximum absolute diff |8-2| = 6 > 4.
[8,2,4,7] with maximum absolute diff |8-2| = 6 > 4.
[2] with maximum absolute diff |2-2| = 0 <= 4.
[2,4] with maximum absolute diff |2-4| = 2 <= 4.
[2,4,7] with maximum absolute diff |2-7| = 5 > 4.
[4] with maximum absolute diff |4-4| = 0 <= 4.
[4,7] with maximum absolute diff |4-7| = 3 <= 4.
[7] with maximum absolute diff |7-7| = 0 <= 4.
Therefore, the size of the longest subarray is 2.

Example 2:
Input: nums = [10,1,2,4,7,2], limit = 5
Output: 4
Explanation: The subarray [2,4,7,2] is the longest since the maximum absolute diff is |2-7| = 5 <= 5.

Example 3:
Input: nums = [4,2,2,2,4,4,2,2], limit = 0
Output: 3

Constraints:
1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9
0 <= limit <= 10^9
'''

# Approach 1: heap
import heapq
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq, maxq = [], []
        res = j = 0
        for i, num in enumerate(nums):
            heapq.heappush(minq, (num, i))
            heapq.heappush(maxq, (-num, i))
            while -maxq[0][0] - minq[0][0] > limit:
                j = min(minq[0][1], maxq[0][1]) + 1
                while minq and minq[0][1] < j:
                    heapq.heappop(minq)
                while maxq and maxq[0][1] < j:
                    heapq.heappop(maxq)
            res = max(res, i - j + 1)
        return res

# Approach 2: deque
from collections import deque
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        minq, maxq = deque(), deque()
        res = l = 0
        for r, num in enumerate(nums):
            while minq and num < minq[-1]:
                minq.pop()
            while maxq and num > maxq[-1]:
                maxq.pop()
            minq.append(num)
            maxq.append(num)
            while maxq[0] - minq[0] > limit:
                if minq[0] == nums[l]:
                    minq.popleft()
                if maxq[0] == nums[l]:
                    maxq.popleft()
                l += 1
            res = max(res, r - l + 1)
        return res
