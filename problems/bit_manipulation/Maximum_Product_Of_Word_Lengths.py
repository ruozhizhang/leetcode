'''
https://leetcode.com/problems/maximum-product-of-word-lengths/

Given a string array words, find the maximum value of length(word[i]) *
length(word[j]) where the two words do not share common letters. You may assume
that each word will contain only lower case letters. If no such two words exist,
return 0.

Example 1:
Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

Example 2:
Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".

Example 3:
Input: ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
'''

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        values = [0] * n
        for i, word in enumerate(words):
            for ch in word:
                values[i] |= 1 << (ord(ch) - ord('a'))

        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if values[i] & values[j] == 0 and len(words[i]) * len(words[j]) > res:
                    res = len(words[i]) * len(words[j])
        return res
