'''
https://leetcode.com/problems/word-ladder/

Given two words (beginWord and endWord), and a dictionary's word list, find the length
of shortest transformation sequence from beginWord to endWord, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list.

Note:
Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
'''

from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList:
            return 0
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        while q:
            cur, level = q.popleft()
            if cur == endWord:
                return level
            for nxt in self.getNeighbors(cur, wordList):
                if nxt not in visited:
                    q.append((nxt, level + 1))
                    visited.add(nxt)
        return 0

    def getNeighbors(self, word, wordList):
        n = len(word)
        res = []
        for i in range(n):
            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch != word[i]:
                    newWord = word[:i] + ch + word[i+1:]
                    if newWord in wordList:
                        res.append(newWord)
        return res
