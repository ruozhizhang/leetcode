'''
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of
each bar is 1, compute how much water it is able to trap after raining.

Example:
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
'''

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        biggest_left = [-1] * n
        for i in range(1, n):
            biggest_left[i] = max(biggest_left[i - 1], height[i - 1])

        biggest_right = [-1] * n
        for i in range(n - 2, -1, -1):
            biggest_right[i] = max(biggest_right[i + 1], height[i + 1])

        res = 0
        for i in range(1, n - 1):
            temp = min(biggest_left[i], biggest_right[i]) - height[i]
            res += max(temp, 0)
        return res
