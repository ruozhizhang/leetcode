'''
https://leetcode.com/problems/cheapest-flights-within-k-stops/

There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
Now given all the cities and flights, together with starting city src and the destination dst,
your task is to find the cheapest price from src to dst with up to k stops.
If there is no such route, output -1.

Example 1:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200

Example 2:
Input:
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500

Note:
The number of nodes n will be in range [1, 100], with nodes labeled from 0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.
'''

# Approach 1
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # format change of the graph
        f = [[] for _ in range(n)]
        for s, d, p in flights:
            f[s].append((d, p))
        # global optimal result
        res = float('inf')
        # searching initial state
        stack = [(src, K, 0)]
        # if there is an available path to search
        while stack:
            cur, k, cost = stack.pop()
            # if current path has ended and target is found, update global optimal result then move on to next path
            if cur == dst:
                res = min(res, cost)
                continue
            # if current path has ended and target is not found, just move on to next path
            if k < 0:
                continue
            # if current path has not ended, continue with current path
            for nxt, p in f[cur]:
                # if this path does not help with global optimal result, prune it, do not proceed in this direction
                if p + cost >= res:
                    continue
                stack.append((nxt, k - 1, cost + p))
        return res if res != float('inf') else -1

# Approach 2
from collections import defaultdict
from functools import lru_cache
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        d = defaultdict(list)
        for a, b, p in flights:
            d[a].append((b, p))

        @lru_cache(None)
        def helper(src, dst, k):
            if src == dst:
                return 0
            if k < 0:
                return float('inf')

            res = float('inf')
            for nxt, p in d[src]:
                res = min(res, p + helper(nxt, dst, k - 1))
            return res

        res = helper(src, dst, K)
        return res if res != float('inf') else -1
