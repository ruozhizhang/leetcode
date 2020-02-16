# https://leetcode.com/problems/super-egg-drop/

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        f = [[0] * (N + 1) for _ in range(K + 1)]

        for i in range(1, K + 1):
            f[i][1] = 1
        for j in range(1, N + 1):
            f[1][j] = j

        if K == 1 or N == 1:
            return f[K][N]

        for i in range(2, K + 1):
            for j in range(2, N + 1):
                f[i][j] = f[i - 1][j - 1] + f[i][j - 1] + 1

                if i == K and f[i][j] >= N:
                    return j
