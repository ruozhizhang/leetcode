'''
https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/

Given a matrix, and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some
coordinate that is different: for example, if x1 != x1'.

Example 1:
Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.

Example 2:
Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.

Note:
1 <= matrix.length <= 300
1 <= matrix[0].length <= 300
-1000 <= matrix[i] <= 1000
-10^8 <= target <= 10^8
'''

from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, A: List[List[int]], target: int) -> int:
        m, n = len(A), len(A[0])
        rowSum = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                rowSum[i][j] = A[i][j] + (rowSum[i][j - 1] if j > 0 else 0)

        res = 0
        for i in range(n):
            for j in range(i, n):
                preSum = 0
                d = defaultdict(int)
                d[0] = 1
                for k in range(m):
                    preSum += rowSum[k][j] - (rowSum[k][i - 1] if i > 0 else 0)
                    if preSum - target in d:
                        res += d[preSum - target]
                    d[preSum] += 1
        return res
