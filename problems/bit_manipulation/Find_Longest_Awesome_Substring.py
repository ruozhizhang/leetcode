'''
https://leetcode.com/problems/find-longest-awesome-substring/

Given a string s. An awesome substring is a non-empty substring of s such that we
can make any number of swaps in order to make it palindrome.

Return the length of the maximum length awesome substring of s.


Example 1:
Input: s = "3242415"
Output: 5
Explanation: "24241" is the longest awesome substring, we can form the palindrome
"24142" with some swaps.

Example 2:
Input: s = "12345678"
Output: 1

Example 3:
Input: s = "213123"
Output: 6
Explanation: "213123" is the longest awesome substring, we can form the palindrome
"231132" with some swaps.

Example 4:
Input: s = "00"
Output: 2

Constraints:
1 <= s.length <= 10^5
s consists only of digits.
'''

class Solution:
    def longestAwesome(self, s: str) -> int:
        res = 0
        mask = 0
        d = {0 : -1}
        for i in range(len(s)):
            pos = ord(s[i]) - 48
            mask ^= (1 << pos)
            for j in range(11):
                newMask = (mask ^ (1 << j)) & 1023
                if newMask in d:
                    res = max(res, i - d[newMask])
            if mask not in d:
                d[mask] = i
        return res
