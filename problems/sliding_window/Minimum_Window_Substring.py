'''
https://leetcode.com/problems/minimum-window-substring/

Given a string S and a string T, find the minimum window in S which will contain
all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique
minimum window in S.
'''

from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = Counter(t)
        countS = Counter()
        lenT = len(countT)
        matchNum = 0
        l = 0
        res = ''
        for r in range(len(s)):
            countS[s[r]] += 1
            if countS[s[r]] == countT[s[r]]:
                matchNum += 1
                while matchNum == lenT:
                    countS[s[j]] -= 1
                    if s[j] in countT and countS[s[j]] < countT[s[j]]:
                        matchNum -= 1
                        if not res or i - j + 1 < len(res):
                            res = s[j:i+1]
                    j += 1
        return res
