'''
https://leetcode.com/problems/perfect-squares/

Given a positive integer n, find the least number of perfect square numbers (for example,
1, 4, 9, 16, ...) which sum to n.

Example 1:
Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.

Example 2:
Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
'''

# APPROACH 1: DP
import math
class Solution:
    def numSquares(self, n: int) -> int:
        f = [i for i in range(n + 1)]
        for i in range(2, n + 1):
            if int(math.sqrt(i)) ** 2 == i:
                f[i] = 1
                continue
            j = 1
            while i - j ** 2 > 0:
                f[i] = min(f[i], 1 + f[i - j ** 2])
                j += 1
        return f[n]

# APPROACH 2: BFS
class Solution:
    def numSquares(self, n: int) -> int:
        level = {n}
        res = 0
        while level:
            newLevel = set()
            for num in level:
                if num == 0:
                    return res
                i = 1
                while num >= i ** 2:
                    newLevel.add(num - i ** 2)
                    i += 1
            level = newLevel
            res += 1
