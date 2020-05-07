'''
https://leetcode.com/problems/number-of-islands-ii/

A 2d grid map of m rows and n columns is initially filled with water. We may perform
an addLand operation which turns the water at position (row, col) into a land. Given
a list of positions to operate, count the number of islands after each addLand operation.
An island is surrounded by water and is formed by connecting adjacent lands horizontally
or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:
Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:
Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1
represents land).
0 0 0
0 0 0
0 0 0

Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.
1 0 0
0 0 0   Number of islands = 1
0 0 0

Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.
1 1 0
0 0 0   Number of islands = 1
0 0 0

Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.
1 1 0
0 0 1   Number of islands = 2
0 0 0

Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.
1 1 0
0 0 1   Number of islands = 3
0 1 0

Follow up:
Can you do it in time complexity O(k log mn), where k is the length of the positions?
'''

'''
Algorithm: Union Find.
Time complexity: O(m * n)
'''

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        parent = [-1] * (m * n)
        rank = [0] * (m * n)

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

        res = []
        for i, j in positions:
            if parent[i * n + j] != -1:
                res.append(res[-1])
                continue
            num = 1 + res[-1] if res else 1
            parent[i * n + j] = i * n + j
            for del_i, del_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nxt_i, nxt_j = i + del_i, j + del_j
                if 0 <= nxt_i < m and 0 <= nxt_j < n and parent[nxt_i * n + nxt_j] != -1:
                    if union(i * n + j, nxt_i * n + nxt_j):
                        num -= 1
            res.append(num)
        return res
