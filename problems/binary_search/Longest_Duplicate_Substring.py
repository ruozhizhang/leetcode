'''
https://leetcode.com/problems/longest-duplicate-substring/

Given a string S, consider all duplicated substrings: (contiguous) substrings of S
that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not
have a duplicated substring, the answer is "".)

Example 1:
Input: "banana"
Output: "ana"

Example 2:
Input: "abcd"
Output: ""

Note:
2 <= S.length <= 10^5
S consists of lowercase English letters.
'''

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        nums = [ord(ch) - ord('a') for ch in S]

        l, r = 1, len(S)
        while l + 1 < r:
            mid = l + (r - l) // 2
            if self.helper(S, mid, nums) != '':
                l = mid
            else:
                r = mid

        sr = self.helper(S, r, nums)
        if sr != '':
            return sr
        sl = self.helper(S, l, nums)
        if sl != '':
            return sl
        return ''

    def helper(self, S, l, nums):
        MOD = 2 ** 32
        # hash of S[:l]
        h = 0
        for i in range(l):
            h = (h * 26 + nums[i]) % MOD

        MUL = pow(26, l, MOD)
        seen = {h}
        for i in range(l, len(S)):
            h = (h * 26 + nums[i] - nums[i - l] * MUL) % MOD
            if h in seen:
                return S[i-l+1:i+1]
            seen.add(h)
        return ''
