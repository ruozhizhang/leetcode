'''
https://leetcode.com/problems/tree-diameter/

Given an undirected tree, return its diameter: the number of edges in a longest path in
that tree.

The tree is given as an array of edges where edges[i] = [u, v] is a bidirectional edge
between nodes u and v.  Each node has labels in the set {0, 1, ..., edges.length}.

Constraints:
0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
The given edges form an undirected tree.
'''

from collections import defaultdict
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        '''
        algorithm: start from any node A, traverse the graph to find the furthest node B
        start from B, traverse the graph to find the furthest node C
        distance between B and C is the diameter
        '''
        neighbors = defaultdict(list)
        for a, b in edges:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(start):
            stack = [(start, 0)]
            seen = set([start])
            furthest = 0
            maxLen = 0
            while stack:
                i, l = stack.pop()
                if l > maxLen:
                    maxLen = l
                    furthest = i
                for j in neighbors[i]:
                    if j not in seen:
                        stack.append((j, l + 1))
                        seen.add(j)
            return maxLen, furthest

        _, furthest = dfs(0)
        maxLen, _ = dfs(furthest)
        return maxLen
