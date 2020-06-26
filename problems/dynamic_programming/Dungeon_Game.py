'''
The demons had captured the princess (P) and imprisoned her in the bottom-right corner
of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant
knight (K) was initially positioned in the top-left room and must fight his way through
the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point
his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers)
upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that
increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only
rightward or downward in each step.


Write a function to determine the knight's minimum initial health so that he is able to
rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least
7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)

Note:
The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the
bottom-right room where the princess is imprisoned.
'''

class Solution:
    def calculateMinimumHP(self, A: List[List[int]]) -> int:
        if not A or not A[0]:
            return 0

        m, n = len(A), len(A[0])
        f = [[0] * n for _ in range(m)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if i == m - 1 and j == n - 1:
                    f[i][j] = max(-A[i][j], 0) + 1
                elif i == m - 1:
                    f[i][j] = max(f[i][j + 1] - A[i][j], 1)
                elif j == n - 1:
                    f[i][j] = max(f[i + 1][j] - A[i][j], 1)
                else:
                    f[i][j] = max(min(f[i + 1][j], f[i][j + 1]) - A[i][j], 1)
        return f[0][0]
