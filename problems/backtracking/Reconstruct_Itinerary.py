'''
https://leetcode.com/problems/reconstruct-itinerary/

Given a list of airline tickets represented by pairs of departure and arrival airports
[from, to], reconstruct the itinerary in order. All of the tickets belong to a man who
departs from JFK. Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries, you should return the itinerary that has the
smallest lexical order when read as a single string. For example, the itinerary
["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

All airports are represented by three capital letters (IATA code).
You may assume all tickets form at least one valid itinerary.
One must use all the tickets once and only once.

Example 1:
Input: [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

Example 2:
Input: [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Output: ["JFK","ATL","JFK","SFO","ATL","SFO"]
Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
             But it is larger in lexical order.
'''

from collections import defaultdict, Counter
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if not tickets:
            return []
        d = defaultdict(list)
        count = Counter([tuple(t) for t in tickets])
        for start, end in sorted(tickets):
            d[start].append(end)

        res = ['JFK']
        self.helper(d, 'JFK', count, len(tickets), res)
        return res

    def helper(self, d, cur, count, l, path):
        if len(path) == l + 1:
            return True

        if cur not in d:
            return False

        for nxt in d[cur]:
            if (cur, nxt) in count and count[(cur, nxt)] > 0:
                path.append(nxt)
                count[(cur, nxt)] -= 1
                res = self.helper(d, nxt, count, l, path)
                if res:
                    return True
                count[(cur, nxt)] += 1
                path.pop()
        return False
