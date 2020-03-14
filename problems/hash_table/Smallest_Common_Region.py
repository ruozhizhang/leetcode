'''
https://leetcode.com/problems/smallest-common-region/

You are given some lists of regions where the first region of each list includes all other
regions in that list.

Naturally, if a region X contains another region Y then X is bigger than Y. Also by
definition a region X contains itself.

Given two regions region1, region2, find out the smallest region that contains both of them.

If you are given regions r1, r2 and r3 such that r1 includes r3, it is guaranteed there is
no r2 such that r2 includes r3.

It's guaranteed the smallest region exists.

Example 1:

Input:
regions = [["Earth","North America","South America"],
["North America","United States","Canada"],
["United States","New York","Boston"],
["Canada","Ontario","Quebec"],
["South America","Brazil"]],
region1 = "Quebec",
region2 = "New York"
Output: "North America"

Constraints:
2 <= regions.length <= 10^4
region1 != region2
All strings consist of English letters and spaces with at most 20 letters.
'''

'''
Similar problems:
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
'''

class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        '''
        algorithm:
        1. retrive all the mappings from a region to its parent
        2. starting from region1, go all the way to the top, record all nodes on the path
        into a set
        3. starting from region2, go all the way to the top, return the first node it meets
        that is in the set
        '''
        d = {}
        for region in regions:
            if region[0] not in d:
                d[region[0]] = ''
            for i in range(1, len(region)):
                d[region[i]] = region[0]

        s = set()
        r = region1
        while r in d:
            s.add(r)
            r = d[r]

        r = region2
        while r in d:
            if r in s:
                return r
            r = d[r]
