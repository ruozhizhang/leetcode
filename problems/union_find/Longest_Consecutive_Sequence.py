'''
https://leetcode.com/problems/longest-consecutive-sequence/

Given an unsorted array of integers, find the length of the longest consecutive
elements sequence.

Your algorithm should run in O(n) complexity.

Example:
Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore
its length is 4.
'''

# Approach 1
from collections import defaultdict
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        d = defaultdict(int)
        res = 0
        for num in nums:
            if d[num] != 0:
                continue
            d[num] = 1
            lb, rb = num - d[num - 1], num + d[num + 1]
            if d[lb] > 0:
                d[lb] = rb - lb + 1
            if d[rb] > 0:
                d[rb] = rb - lb + 1
            res = max(res, d[lb], d[rb])
        return res

# Approach 2: Union Find
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        parent = {}
        size = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return 0
            if size[rootX] > size[rootY]:
                rootX, rootY = rootY, rootX
            parent[rootX] = rootY
            size[rootY] += size[rootX]
            return size[rootY]

        res = 1
        for num in nums:
            if num in parent:
                continue
            parent[num] = num
            size[num] = 1
            if num - 1 in parent:
                res = max(res, union(num, num - 1))
            if num + 1 in parent:
                res = max(res, union(num, num + 1))
        return res
