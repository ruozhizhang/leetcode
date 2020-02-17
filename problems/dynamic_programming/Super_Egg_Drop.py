'''
https://leetcode.com/problems/super-egg-drop/

You are given K eggs, and you have access to a building with N floors from 1 to N.

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a
floor higher than F will break, and any egg dropped at or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from any floor
X (with 1 <= X <= N).

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty what F is,
regardless of the initial value of F?


Example 1:

Input: K = 1, N = 2
Output: 2
Explanation:
Drop the egg from floor 1.  If it breaks, we know with certainty that F = 0.
Otherwise, drop the egg from floor 2.  If it breaks, we know with certainty that F = 1.
If it didn't break, then we know with certainty F = 2.
Hence, we needed 2 moves in the worst case to know what F is with certainty.

Example 2:

Input: K = 2, N = 6
Output: 3
Example 3:

Input: K = 3, N = 14
Output: 4


Note:

1 <= K <= 100
1 <= N <= 10000
'''

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        '''
        f[i][j] means with i eggs and j moves, how many floors can be covered
        Range of i eggs: 0 - K
        Range of j moves: 0 - N (for N floors, the max number of needed moves is N)
        '''
        f = [[0] * (N + 1) for _ in range(K + 1)]

        '''
        If only one floor, needed move is 1
        If only one egg, the max number of floors can be covered by j moves is j (just
        try dropping the egg starting from floor 1 until floor j)
        '''
        for i in range(1, K + 1):
            f[i][1] = 1
        for j in range(1, N + 1):
            f[1][j] = j

        if K == 1 or N == 1:
            return f[K][N]

        '''
        Assuming f[i - 1][j - 1] == A and f[i][j - 1] == B, how many floors can f[i][j]
        cover?
        the answer is f[i - 1][j - 1] + f[i][j - 1] + 1 = A + B + 1

        Note that we need to cover the number of floors with certainty, regardless of
        the initial value of F.
        If we try to drop one egg in floor A + 1, there can only be two cases of F here:
        1. F can be greater than or equal to A + 1, then the egg won't break, and then
        we can use f[i][j - 1] moves to cover B more floors
        2. F can be less than A + 1, then the egg will break, and then we can use
        f[i - 1][j] moves to cover A more floors

        So in the range of A + B + 1 floors, no matter what the inital value F is,
        f[i][j] would be able to find it, hence f[i][j] = f[i - 1][j - 1] + f[i][j - 1] + 1
        '''
        for i in range(2, K + 1):
            for j in range(2, N + 1):
                f[i][j] = f[i - 1][j - 1] + f[i][j - 1] + 1

                if i == K and f[i][j] >= N:
                    return j
