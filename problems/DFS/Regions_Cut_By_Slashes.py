'''
https://leetcode.com/problems/regions-cut-by-slashes/

In a N x N grid composed of 1 x 1 squares, each 1 x 1 square consists of a /, \,
or blank space.  These characters divide the square into contiguous regions.

(Note that backslash characters are escaped, so a \ is represented as "\\".)

Return the number of regions.

Example 1:
Input:
[
  " /",
  "/ "
]
Output: 2

Example 2:
Input:
[
  " /",
  "  "
]
Output: 1

Example 3:
Input:
[
  "\\/",
  "/\\"
]
Output: 4
Explanation: (Recall that because \ characters are escaped, "\\/" refers to \/,
and "/\\" refers to /\.)

Example 4:
Input:
[
  "/\\",
  "\\/"
]
Output: 5
Explanation: (Recall that because \ characters are escaped, "/\\" refers to /\,
and "\\/" refers to \/.)

Example 5:
Input:
[
  "//",
  "/ "
]
Output: 3

Note:
1 <= grid.length == grid[0].length <= 30
grid[i][j] is either '/', '\', or ' '.
'''

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        A = [[0] * (3 * n) for _ in range(3 * n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    A[3 * i][3 * j + 2] = A[3 * i + 1][3 * j + 1] = A[3 * i + 2][3 * j] = 1
                elif grid[i][j] == '\\':
                    A[3 * i][3 * j] = A[3 * i + 1][3 * j + 1] = A[3 * i + 2][3 * j + 2] = 1

        stack = []
        res = 0
        for i in range(3 * n):
            for j in range(3 * n):
                if A[i][j] == 1:
                    continue
                stack.append((i, j))
                A[i][j] = 1
                res += 1
                while stack:
                    cur_i, cur_j = stack.pop()
                    for del_i, del_j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        nxt_i, nxt_j = cur_i + del_i, cur_j + del_j
                        if 0 <= nxt_i < 3 * n and 0 <= nxt_j < 3 * n and A[nxt_i][nxt_j] == 0:
                            stack.append((nxt_i, nxt_j))
                            A[nxt_i][nxt_j] = 1
        return res
