'''
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/

Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
'''

from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = defaultdict(int)
        res = 0
        l = 0
        for r in range(len(s)):
            d[s[r]] += 1
            while len(d) > k:
                d[s[l]] -= 1
                if d[s[l]] == 0:
                    del d[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res
