'''
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, find the longest palindromic substring in s. You may assume that
the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        n = len(s)
        res = 0
        start = end = 0
        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > res:
                    res = r - l + 1
                    start, end = l, r
                l -= 1
                r += 1

        for i in range(n):
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l + 1 > res:
                    res = r - l + 1
                    start, end = l, r
                l -= 1
                r += 1

        return s[start:end + 1]
