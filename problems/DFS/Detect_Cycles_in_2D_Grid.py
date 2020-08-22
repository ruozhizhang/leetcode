'''
https://leetcode.com/problems/detect-cycles-in-2d-grid/

Given a 2D array of characters grid of size m x n, you need to find if there exists any cycle consisting
of the same value in grid.

A cycle is a path of length 4 or more in the grid that starts and ends at the same cell. From a given
cell, you can move to one of the cells adjacent to it - in one of the four directions (up, down, left,
or right), if it has the same value of the current cell.

Also, you cannot move to the cell that you visited in your last move. For example, the cycle (1, 1)
-> (1, 2) -> (1, 1) is invalid because from (1, 2) we visited (1, 1) which was the last visited cell.

Return true if any cycle of the same value exists in grid, otherwise, return false.

Example 1:
Input: grid = [["a","a","a","a"],["a","b","b","a"],["a","b","b","a"],["a","a","a","a"]]
Output: true
Explanation: There are two valid cycles shown in different colors in the image below:

Example 2:
Input: grid = [["c","c","c","a"],["c","d","c","c"],["c","c","e","c"],["f","c","c","c"]]
Output: true
Explanation: There is only one valid cycle highlighted in the image below:

Example 3:
Input: grid = [["a","b","b"],["b","z","b"],["b","b","a"]]
Output: false

Constraints:
m == grid.length
n == grid[i].length
1 <= m <= 500
1 <= n <= 500
grid consists only of lowercase English letters.
'''

class Solution:
    def containsCycle(self, A: List[List[str]]) -> bool:
        m, n = len(A), len(A[0])
        visited = set()
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited and self.dfs(A, i, j, -1, -1, visited):
                    return True
        return False

    def dfs(self, A, x, y, lx, ly, visited):
        if (x, y) in visited:
            return True

        visited.add((x, y))
        m, n = len(A), len(A[0])
        for del_x, del_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nxt_x, nxt_y = x + del_x, y + del_y
            if 0 <= nxt_x < m and 0 <= nxt_y < n and A[nxt_x][nxt_y] == A[x][y] and (nxt_x != lx or nxt_y != ly):
                if self.dfs(A, nxt_x, nxt_y, x, y, visited):
                    return True
        return False
