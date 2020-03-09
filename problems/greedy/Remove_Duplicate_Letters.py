'''
https://leetcode.com/problems/remove-duplicate-letters/

Given a string which contains only lowercase letters, remove duplicate letters so that every
letter appears once and only once. You must make sure your result is the smallest in
lexicographical order among all possible results.

Example 1:

Input: "bcabc"
Output: "abc"
Example 2:

Input: "cbacdcbc"
Output: "acdb"
'''

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        '''
        algorithm: for each letter, if it is a peak element and there is more the same letter, it
        can be removed

        1. use stack to check peak element
        2. seen means the temporary availability of the letters, if seen[ch] is True, it means we
        already know the position of ch, it could be reverted later if a smaller letter is found
        '''
        counts = [0] * 26
        seen = [False] * 26
        stack = []

        for ch in s:
            counts[ord(ch) - ord('a')] += 1

        for ch in s:
            counts[ord(ch) - ord('a')] -= 1

            if seen[ord(ch) - ord('a')]:
                continue

            while stack and stack[-1] > ch and counts[ord(stack[-1]) - ord('a')] > 0:
                seen[ord(stack[-1]) - ord('a')] = False
                stack.pop()
            stack.append(ch)
            seen[ord(ch) - ord('a')] = True

        return ''.join(stack)
