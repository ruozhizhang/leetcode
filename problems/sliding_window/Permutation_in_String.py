'''
https://leetcode.com/problems/permutation-in-string/

Given two strings s1 and s2, write a function to return true if s2 contains the
permutation of s1. In other words, one of the first string's permutations is the
substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
'''

from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if not s1:
            return True
        countS1 = Counter(s1)
        countS2 = Counter()
        matchNum = 0
        l = 0
        for r in range(len(s2)):
            countS2[s2[r]] += 1
            if countS2[s2[r]] == countS1[s2[r]]:
                matchNum += 1
                if matchNum == len(countS1):
                    return True
            while countS2[s2[r]] > countS1[s2[r]]:
                if countS2[s2[l]] == countS1[s2[l]]:
                    matchNum -= 1
                countS2[s2[l]] -= 1
                l += 1
        return False
