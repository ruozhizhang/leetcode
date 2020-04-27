'''
https://leetcode.com/problems/sliding-window-median/

Median is the middle value in an ordered integer list. If the size of the list is
even, there is no middle value. So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5

Given an array nums, there is a sliding window of size k which is moving from
the very left of the array to the very right. You can only see the k numbers in
the window. Each time the sliding window moves right by one position. Your job
is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size
for non-empty array.
Answers within 10^-5 of the actual value will be accepted as correct.
'''

import heapq
class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        res = []
        minHalf, maxHalf = [], []
        for i in range(k):
            heapq.heappush(minHalf, (-nums[i], i))
        for _ in range(k - k // 2):
            self.move(minHalf, maxHalf)
        res.append(self.getMedian(minHalf, maxHalf, k))
        for i in range(k, len(nums)):
            if nums[i] >= maxHalf[0][0]:
                heapq.heappush(maxHalf, (nums[i], i))
                if nums[i - k] <= maxHalf[0][0]:
                    self.move(maxHalf, minHalf)
            else:
                heapq.heappush(minHalf, (-nums[i], i))
                if nums[i - k] >= maxHalf[0][0]:
                    self.move(minHalf, maxHalf)
            while minHalf and minHalf[0][1] <= i - k:
                heapq.heappop(minHalf)
            while maxHalf and maxHalf[0][1] <= i - k:
                heapq.heappop(maxHalf)
            res.append(self.getMedian(minHalf, maxHalf, k))
        return res

    def move(self, h1, h2):
        num, i = heapq.heappop(h1)
        heapq.heappush(h2, (-num, i))

    def getMedian(self, h1, h2, k):
        return h2[0][0] * 1.0 if k % 2 else (h2[0][0] - h1[0][0]) / 2.0
