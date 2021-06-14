'''
https://leetcode.com/problems/path-with-maximum-minimum-value/

Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at[0, 0] 
and ending at[R-1, C-1].

The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 
is 4.

A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 
cardinal directions(north, east, west, south).

Example 1:
Input: [[5, 4, 5], [1, 2, 6], [7, 4, 6]]
Output: 4
Explanation:
The path with the maximum score is highlighted in yellow.

Example 2:
Input: [[2, 2, 1, 2, 2, 2], [1, 2, 2, 2, 1, 2]]
Output: 2

Example 3:
Input: [[3, 4, 6, 3, 4], [0, 2, 1, 1, 7], [8, 8, 3, 2, 7],
        [3, 2, 4, 9, 8], [4, 1, 2, 0, 0], [4, 6, 5, 4, 3]]
Output: 3

Note:
1 <= R, C <= 100
0 <= A[i][j] <= 10 ^ 9
'''

# Approach 1: Dijkstra's algorithm
import heapq
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        heap = [(-A[0][0], 0, 0)]
        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True
        while heap:
            curScore, x, y = heapq.heappop(heap)
            if x == m - 1 and y == n - 1:
                return -curScore
            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    visited[nx][ny] = True
                    heapq.heappush(heap, (max(curScore, -A[nx][ny]), nx, ny))

# Approach 2: Union Find
class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        nums = sorted((-A[i][j], i, j) for i in range(m) for j in range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[px] = py
            return True

        parent = [-1] * (m * n)
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for num, i, j in nums:
            parent[i * n + j] = i * n + j
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and parent[ni * n + nj] != -1:
                    union(i * n + j, ni * n + nj)

            if parent[0] != -1 and parent[m * n - 1] != -1 and find(0) == find(m * n - 1):
                return -num

        return A[0][0]