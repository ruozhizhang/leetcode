'''
https://leetcode.com/problems/magnetic-force-between-two-balls/

In universe Earth C-137, Rick discovered a special form of magnetic force between two balls if they are put in 
his new invented basket. Rick has n empty baskets, the ith basket is at position[i], Morty has m balls and needs
to distribute the balls into the baskets such that the minimum magnetic force between any two balls is maximum.

Rick stated that magnetic force between two different balls at positions x and y is |x - y|.

Given the integer array position and the integer m. Return the required force.

Example 1:
Input: position = [1,2,3,4,7], m = 3
Output: 3
Explanation: Distributing the 3 balls into baskets 1, 4 and 7 will make the magnetic force between ball pairs 
[3, 3, 6]. The minimum magnetic force is 3. We cannot achieve a larger minimum magnetic force than 3.

Example 2:
Input: position = [5,4,3,2,1,1000000000], m = 2
Output: 999999999
Explanation: We can use baskets 1 and 1000000000.

Constraints:
n == position.length
2 <= n <= 10^5
1 <= position[i] <= 10^9
All integers in position are distinct.
2 <= m <= position.length
'''

# Solution 1
import bisect
class Solution:
    def maxDistance(self, A: List[int], m: int) -> int:
        A.sort()
        if m == 2:
            return A[-1] - A[0]
        l = 1
        r = (A[-1] - A[0]) // (m - 2)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.goodDis(A, m, mid):
                l = mid
            else:
                r = mid

        if self.goodDis(A, m, r):
            return r
        return l

    def goodDis(self, A, m, d):
        cur = A[0]
        res = True
        for _ in range(m - 1):
            nxt = cur + d
            if nxt > A[-1]:
                res = False
                break
            ind = bisect.bisect_left(A, nxt)
            cur = A[ind]
        return res

# solution 2
class Solution:
    def maxDistance(self, A: List[int], m: int) -> int:
        A.sort()
        if m == 2:
            return A[-1] - A[0]
        l = 1
        r = (A[-1] - A[0]) // (m - 2)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.goodDis(A, m, mid):
                l = mid
            else:
                r = mid

        if self.goodDis(A, m, r):
            return r
        return l

    def goodDis(self, A, m, d):
        cur = A[0]
        count = 0
        for i in range(1, len(A)):
            if A[i] - cur >= d:
                cur = A[i]
                count += 1
                if count == m - 1:
                    return True
        return False
