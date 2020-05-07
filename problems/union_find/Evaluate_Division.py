'''
https://leetcode.com/problems/evaluate-division/

Equations are given in the format A / B = k, where A and B are variables represented
as strings, and k is a real number (floating point number). Given some queries, return
the answers. If the answer does not exist, return -1.0.

Example:
Given a / b = 2.0, b / c = 3.0.
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ? .
return [6.0, 0.5, -1.0, 1.0, -1.0 ].

The input is: vector<pair<string, string>> equations, vector<double>& values,
vector<pair<string, string>> queries , where equations.size() == values.size(),
and the values are positive. This represents the equations. Return vector<double>.

According to the example above:
equations = [ ["a", "b"], ["b", "c"] ],
values = [2.0, 3.0],
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ].

The input is always valid. You may assume that evaluating the queries will result in no
division by zero and there is no contradiction.
'''

# Approach 1: DFS
from collections import defaultdict
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # build graph
        graph = defaultdict(dict)
        for i in range(len(equations)):
            a, b = equations[i]
            r = values[i]
            graph[a][b] = r
            graph[b][a] = 1 / r

        res = []
        for start, end in queries:
            res.append(self.dfs(graph, start, end, set([start])))
        return res

    def dfs(self, graph, start, end, visited):
        if start not in graph:
            return -1.0
        if start == end:
            return 1.0
        for nxt, r in graph[start].items():
            if nxt not in visited:
                visited.add(nxt)
                subPathRatio = self.dfs(graph, nxt, end, visited)
                if subPathRatio != -1.0:
                    return r * subPathRatio
        return -1.0

# Approach 2: Union Find
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        parent = {}
        ratio = {}

        def find(x):
            if parent[x] != x:
                parent[x], ra = find(parent[x])
                ratio[x] *= ra
            return parent[x], ratio[x]

        def union(x, y, r):
            rootX, raX = find(x)
            rootY, raY = find(y)
            if rootX == rootY:
                return False
            parent[rootX] = rootY
            ratio[rootX] = raY / raX * r
            return True

        for i in range(len(equations)):
            x, y = equations[i]
            r = values[i]
            if x not in parent:
                parent[x] = x
                ratio[x] = 1.0
            if y not in parent:
                parent[y] = y
                ratio[y] = 1.0
            union(x, y, r)

        res = []
        for x, y in queries:
            if x in parent and y in parent and find(x)[0] == find(y)[0]:
                res.append(ratio[x] / ratio[y])
            else:
                res.append(-1.0)
        return res
