'''
https://leetcode.com/problems/minimum-window-subsequence/

Given strings S and T, find the minimum (contiguous) substring W of S, so that T
is a subsequence of W.

If there is no such window in S that covers all characters in T, return the empty
string "". If there are multiple such minimum-length windows, return the one with
the left-most starting index.

Example 1:
Input:
S = "abcdebdde", T = "bde"
Output: "bcde"
Explanation:
"bcde" is the answer because it occurs before "bdde" which has the same length.
"deb" is not a smaller window because the elements of T in the window must occur in order.

Note:
All the strings in the input will only contain lowercase letters.
The length of S will be in the range [1, 20000].
The length of T will be in the range [1, 100].
'''

class Solution:
    def minWindow(self, S: str, T: str) -> str:
        l = 0
        res = ''
        while l < len(S):
            r = self.findNextWindow(S, T, l)
            if r == -1:
                break
            l = self.reduceWindow(S, T, r)
            if not res or r - l + 1 < len(res):
                res = S[l:r+1]
            l += 1
        return res

    def findNextWindow(self, S, T, l):
        i, j = l, 0
        while i < len(S) and j < len(T):
            if S[i] == T[j]:
                j += 1
            i += 1
        return i - 1 if j == len(T) else -1

    def reduceWindow(self, S, T, r):
        i, j = r, len(T) - 1
        while i >= 0 and j >= 0:
            if S[i] == T[j]:
                j -= 1
            i -= 1
        return i + 1
