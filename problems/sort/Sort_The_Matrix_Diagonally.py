'''
https://leetcode.com/problems/sort-the-matrix-diagonally/

Given a m * n matrix mat of integers, sort it diagonally in ascending order from
the top-left to the bottom-right then return the sorted array.

Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]

Constraints:
m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100
'''

'''
Algorithm:
1. Store all coordinates in the first row and first column in a list, these will
be the starting point of each diagonal
2. For each diagonal, push all the values into a heap, then pop and put to the
corresponding position in ascending order

Time complexity: each node will be pushed into heap and popped out once, so
complexity is O(MN * logL) with L to be min(M, N) (The max number of nodes in
the heap at the same time is the longest length of a diagonal, which is min(M,
N))
Space complexity: O(M + N) to store all starting points, O(L) for the heap,
total is O(M + N) + O(L) = O(M + N)
'''

import heapq
class Solution:
    def diagonalSort(self, A: List[List[int]]) -> List[List[int]]:
        m, n = len(A), len(A[0])
        start = []
        for i in range(m):
            start.append((i, 0))
        for j in range(1, n):
            start.append((0, j))

        q = []
        for x, y in start:
            b, e = x, y
            while x < m and y < n:
                heapq.heappush(q, A[x][y])
                x += 1
                y += 1

            while q:
                A[b][e] = heapq.heappop(q)
                b += 1
                e += 1
        return A
