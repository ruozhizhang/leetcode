'''
https://leetcode.com/problems/largest-1-bordered-square/

Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid
that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.

Example 1:
Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9

Example 2:
Input: grid = [[1,1,0,0]]
Output: 1

Constraints:
1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] is 0 or 1
'''

class Solution:
    def largest1BorderedSquare(self, A: List[List[int]]) -> int:
        '''
        algorithm:
        1. calculate the number of consecutive 1s starting from each node to
        the right and to the bottom using DP
        2. for each node, think it as the top left node of the square,
        starting from the minimum of right and down, we reach the possible top right and
        bottom left nodes of the square, check the down of top right and right of bottom
        left node to see if they are enough to form a square, return the max possible
        square
        '''
        m, n = len(A), len(A[0])
        down = [[0] * n for _ in range(m)]
        right = [[0] * n for _ in range(m)]

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if A[i][j] == 0:
                    continue

                down[i][j] = 1
                right[i][j] = 1
                if i < m - 1:
                    down[i][j] = max(down[i][j], down[i + 1][j] + 1)
                if j < n - 1:
                    right[i][j] = max(right[i][j], right[i][j + 1] + 1)

        res = 0
        for i in range(m):
            for j in range(n):
                l = min(down[i][j], right[i][j])
                for k in range(l, 0, -1):
                    if right[i + k - 1][j] >= k and down[i][j + k - 1] >= k:
                        res = max(res, k ** 2)
        return res
