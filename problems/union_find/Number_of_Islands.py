'''
https://leetcode.com/problems/number-of-islands/

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
'''

# Approach 1: BFS
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        q = deque()
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    q.append((i, j))
                    grid[i][j] = '0'
                    while q:
                        cur_x, cur_y = q.popleft()
                        for del_x, del_y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                            nxt_x, nxt_y = cur_x + del_x, cur_y + del_y
                            if 0 <= nxt_x < m and 0 <= nxt_y < n and grid[nxt_x][nxt_y] == '1':
                                q.append((nxt_x, nxt_y))
                                grid[nxt_x][nxt_y] = '0'

        return res

# Approach 2: DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        stack = []
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    stack.append((i, j))
                    grid[i][j] = '0'
                    while stack:
                        cur_i, cur_j = stack.pop()
                        for del_i, del_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                            nxt_i, nxt_j = cur_i + del_i, cur_j + del_j
                            if 0 <= nxt_i < m and 0 <= nxt_j < n and grid[nxt_i][nxt_j] == '1':
                                stack.append((nxt_i, nxt_j))
                                grid[nxt_i][nxt_j] = '0'
        return res

# Approach 3: Union Find
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        parent = {}
        rank = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootX] > rank[rootY]:
                parent[rootY] = rootX
            else:
                parent[rootX] = rootY
                rank[rootY] += 1
            return True

        m, n = len(grid), len(grid[0])
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] != '0':
                    parent[i * n + j] = i * n + j
                    rank[i * n + j] = 0
                    res += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    continue
                for del_i, del_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nxt_i, nxt_j = i + del_i, j + del_j
                    if 0 <= nxt_i < m and 0 <= nxt_j < n and grid[nxt_i][nxt_j] == '1':
                        if union(i * n + j, nxt_i * n + nxt_j):
                            res -= 1
                grid[i][j] = '0'

        return res
