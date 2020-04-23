'''
https://leetcode.com/problems/sliding-window-maximum/

Given an array nums, there is a sliding window of size k which is moving from the
very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position. Return the max sliding window.

Follow up:
Could you solve it in linear time?

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
Output: [3,3,5,5,6,7]
Explanation:

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Constraints:
1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length
'''

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        for i in range(k):
            while q and q[-1][0] <= nums[i]:
                q.pop()
            q.append((nums[i], i))
        res.append(q[0][0])
        for i in range(k, len(nums)):
            while q and q[-1][0] <= nums[i]:
                q.pop()
            if q and i - q[0][1] >= k:
                q.popleft()
            q.append((nums[i], i))
            res.append(q[0][0])
        return res
