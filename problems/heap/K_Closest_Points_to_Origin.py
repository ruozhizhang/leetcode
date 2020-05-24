'''
https://leetcode.com/problems/k-closest-points-to-origin/

We have a list of points on the plane.  Find the K closest points to the origin (0, 0).

(Here, the distance between two points on a plane is the Euclidean distance.)

You may return the answer in any order.  The answer is guaranteed to be unique
(except for the order that it is in.)

Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

Note:
1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
'''

# Approach 1 minHeap --- O(nlogK)
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        q = []
        for x, y in points:
            d = x ** 2 + y ** 2
            if len(q) < K:
                heapq.heappush(q, (-d, x, y))
            elif -d > q[0][0]:
                heapq.heapreplace(q, (-d, x, y))
        return [[x, y] for _, x, y in q]

# Approach 2 quickSelect --- O(n)
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        dis = [(x ** 2 + y ** 2, [x, y]) for x, y in points]
        return self.helper(dis, 0, len(dis) - 1, K)

    def helper(self, dis, l, r, k):
        if l == r:
            return [dis[l][1]]

        p = l + (r - l) // 2
        dis[p], dis[r] = dis[r], dis[p]
        j = l
        for i in range(l, r):
            if dis[i][0] <= dis[r][0]:
                dis[i], dis[j] = dis[j], dis[i]
                j += 1
        dis[j], dis[r] = dis[r], dis[j]

        if j - l + 1 == k:
            res = [d[1] for d in dis[l:j+1]]
        elif j - l + 1 > k:
            res = self.helper(dis, l, j - 1, k)
        else:
            res = [d[1] for d in dis[l:j+1]] + self.helper(dis, j + 1, r, k - j + l - 1)
        return res
