'''
https://leetcode.com/problems/palindrome-partitioning-ii/

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:
Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
'''

from collections import defaultdict
class Solution:
    def minCut(self, s: str) -> int:
        d = defaultdict(list)
        n = len(s)
        self.getParlindromes(s, d)
        f = [float('inf') for _ in range(n + 1)]
        f[0] = 0
        # f[i] = min(f[j] + 1 if s[j:i-1] is parlindrome for 0 < j < i)
        # if j == 0, f[i] = 0 b/c the whole string s[:i] is palindrome, no need to cut
        for i in range(1, n + 1):
            for j in d[i - 1]:
                if j == 0:
                    f[i] = 0
                else:
                    f[i] = min(f[i], f[j] + 1)
        return f[n]

    def getParlindromes(self, s, d):
        n = len(s)
        for i in range(n):
            l = r = i
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    d[r].append(l)
                    l -= 1
                    r += 1
                else:
                    break

        for i in range(n):
            l, r = i, i + 1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    d[r].append(l)
                    l -= 1
                    r += 1
                else:
                    break
