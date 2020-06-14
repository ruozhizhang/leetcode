'''
https://leetcode.com/problems/allocate-mailboxes/

Given the array houses and an integer k. where houses[i] is the location of the ith
house along a street, your task is to allocate k mailboxes in the street.

Return the minimum total distance between each house and its nearest mailbox.

The answer is guaranteed to fit in a 32-bit signed integer.

Example 1:
Input: houses = [1,4,8,10,20], k = 3
Output: 5
Explanation: Allocate mailboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| +
|9-8| + |10-9| + |20-20| = 5

Example 2:
Input: houses = [2,3,5,12,18], k = 2
Output: 9
Explanation: Allocate mailboxes in position 3 and 14.
Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| +
|5-3| + |12-14| + |18-14| = 9.

Example 3:
Input: houses = [7,4,6,1], k = 1
Output: 8

Example 4:
Input: houses = [3,6,14,10], k = 4
Output: 0

Constraints:
n == houses.length
1 <= n <= 100
1 <= houses[i] <= 10^4
1 <= k <= n
Array houses contain unique integers.
'''

from functools import lru_cache
class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses.sort()
        cost = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                median = houses[(i + j) // 2]
                for h in range(i, j + 1):
                    cost[i][j] += abs(houses[h] - median)

        @lru_cache(None)
        def dp(i, k):
            if i == n and k == 0:
                return 0
            res = float('inf')
            for j in range(i, n):
                res = min(res, cost[i][j] + dp(j + 1, k - 1))
            return res

        return dp(0, k)
