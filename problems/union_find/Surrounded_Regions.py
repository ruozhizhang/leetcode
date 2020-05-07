'''
https://leetcode.com/problems/surrounded-regions/

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded
by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
X X X X
X O O X
X X O X
X O X X

After running your function, the board should be:
X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O' on the border
of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not
connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if
they are adjacent cells connected horizontally or vertically.
'''

# Approach 1: DFS
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])
        s = []
        for i in [0, m - 1]:
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'Z'
                    s.append((i, j))

        for i in range(m):
            for j in [0, n - 1]:
                if board[i][j] == 'O':
                    board[i][j] = 'Z'
                    s.append((i, j))

        while s:
            cur_x, cur_y = s.pop()
            for del_x, del_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nxt_x, nxt_y = cur_x + del_x, cur_y + del_y
                if 0 <= nxt_x < m and 0 <= nxt_y < n and board[nxt_x][nxt_y] == 'O':
                    board[nxt_x][nxt_y] = 'Z'
                    s.append((nxt_x, nxt_y))

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'

                if board[i][j] == 'Z':
                    board[i][j] = 'O'

# Approach 2: Union Find
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        parent = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    parent.append(i * n + j)
                else:
                    parent.append(-1)
        edge = [False] * (m * n)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            if edge[x]:
                edge[parent[x]] = True
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False
            parent[rootX] = rootY
            if edge[rootX]:
                edge[rootY] = True
            return True

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    edge[i * n + j] = True
                if i > 0 and board[i - 1][j] == 'O':
                    union(i * n + j, (i - 1) * n + j)
                if j > 0 and board[i][j - 1] == 'O':
                    union(i * n + j, i * n + j - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    continue
                if not edge[find(i * n + j)]:
                    board[i][j] = 'X'
