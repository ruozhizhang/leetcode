'''
https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down.
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is
not allowed).

Example 1:
Input: nums =
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: nums =
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
'''

# Approach 1: DFS with memoization
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        res = 0
        m, n = len(matrix), len(matrix[0])
        cache = {}
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, i, j, cache))
        return res

    def dfs(self, matrix, i, j, cache):
        if (i, j) in cache:
            return cache[(i, j)]
        m, n = len(matrix), len(matrix[0])
        res = 1
        for del_i, del_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nxt_i, nxt_j = i + del_i, j + del_j
            if 0 <= nxt_i < m and 0 <= nxt_j < n and matrix[nxt_i][nxt_j] > matrix[i][j]:
                res = max(res, 1 + self.dfs(matrix, nxt_i, nxt_j, cache))
        cache[(i, j)] = res
        return res

# Approach 2: Topological sort
from collections import deque
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        indegree = [[0] * n for _ in range(m)]
        q = deque()
        # get indegree of each node and add nodes with indegree 0 into the queue
        for i in range(m):
            for j in range(n):
                for del_i, del_j in dirs:
                    nxt_i, nxt_j = i + del_i, j + del_j
                    if 0 <= nxt_i < m and 0 <= nxt_j < n and matrix[nxt_i][nxt_j] < matrix[i][j]:
                        indegree[i][j] += 1
                if indegree[i][j] == 0:
                    q.append((i, j))

        res = 0
        while q:
            res += 1
            for _ in range(len(q)):
                i, j = q.popleft()
                for del_i, del_j in dirs:
                    nxt_i, nxt_j = i + del_i, j + del_j
                    if 0 <= nxt_i < m and 0 <= nxt_j < n and matrix[nxt_i][nxt_j] > matrix[i][j]:
                        indegree[nxt_i][nxt_j] -= 1
                        if indegree[nxt_i][nxt_j] == 0:
                            q.append((nxt_i, nxt_j))
        return res
