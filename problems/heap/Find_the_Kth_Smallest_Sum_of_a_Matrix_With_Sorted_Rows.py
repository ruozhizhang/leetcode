'''
https://leetcode.com/problems/find-the-kth-smallest-sum-of-a-matrix-with-sorted-rows/

You are given an m * n matrix, mat, and an integer k, which has its rows sorted in
non-decreasing order.

You are allowed to choose exactly 1 element from each row to form an array. Return
the Kth smallest array sum among all possible arrays.

Example 1:
Input: mat = [[1,3,11],[2,4,6]], k = 5
Output: 7
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,2], [1,4], [3,2], [3,4], [1,6]. Where the 5th sum is 7.

Example 2:
Input: mat = [[1,3,11],[2,4,6]], k = 9
Output: 17

Example 3:
Input: mat = [[1,10,10],[1,4,5],[2,3,6]], k = 7
Output: 9
Explanation: Choosing one element from each row, the first k smallest sum are:
[1,1,2], [1,1,3], [1,4,2], [1,4,3], [1,1,6], [1,5,2], [1,5,3]. Where the 7th sum is 9.

Example 4:
Input: mat = [[1,1,10],[2,2,9]], k = 7
Output: 12

Constraints:
m == mat.length
n == mat.length[i]
1 <= m, n <= 40
1 <= k <= min(200, n ^ m)
1 <= mat[i][j] <= 5000
mat[i] is a non decreasing array.
'''

import heapq
class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])
        s = sum(r[0] for r in mat)
        ind = tuple(0 for _ in range(m))
        q = [(s, ind)]
        used = set([ind])

        while k > 1:
            s, ind = heapq.heappop(q)
            for i in range(m):
                j = ind[i]
                if j < n - 1:
                    s_ = s - mat[i][j] + mat[i][j + 1]
                    ind_ = ind[:i] + (j + 1,) + ind[i+1:]
                    if ind_ not in used:
                        heapq.heappush(q, (s_, ind_))
                        used.add(ind_)
            k -= 1

        return q[0][0]
