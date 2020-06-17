'''
https://leetcode.com/problems/largest-divisible-subset/

Given a set of distinct positive integers, find the largest subset such that every
pair (Si, Sj) of elements in this subset satisfies:

Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:
Input: [1,2,3]
Output: [1,2] (of course, [1,3] will also be ok)

Example 2:
Input: [1,2,4,8]
Output: [1,2,4,8]
'''

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        n = len(nums)
        nums.sort()
        f = [(1, i) for i in range(n)]

        maxLen, tail = 1, -1
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and f[i][0] < f[j][0] + 1:
                    f[i] = (f[j][0] + 1, j)
            if f[i][0] > maxLen:
                maxLen, tail = f[i][0], i

        res = []
        while maxLen:
            res.append(nums[tail])
            tail = f[tail][1]
            maxLen -= 1
        return res
