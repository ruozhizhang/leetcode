'''
https://leetcode.com/problems/word-search-ii/

Given a 2D board and a list of words from the dictionary, find all words in the
board.

Each word must be constructed from letters of sequentially adjacent cell, where
"adjacent" cells are those horizontally or vertically neighboring. The same letter
cell may not be used more than once in a word.

Example:
Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Note:
All inputs are consist of lowercase letters a-z.
The values of words are distinct.
'''

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        if not board or not board[0] or not words:
            return []
        m, n = len(board), len(board[0])
        prefix = {}
        for word in words:
            for l in range(1, len(word)):
                if word[:l] not in prefix:
                    prefix[word[:l]] = 0
            prefix[word] = 1

        res = set()
        for i in range(m):
            for j in range(n):
                self.helper(board, i, j, prefix, '', set(), res)
        return list(res)

    def helper(self, board, x, y, prefix, temp, visited, res):
        temp += board[x][y]
        if temp not in prefix:
            return
        elif prefix[temp] == 1:
            res.add(temp)

        visited.add((x, y))
        m, n = len(board), len(board[0])
        for del_x, del_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nxt_x, nxt_y = x + del_x, y + del_y
            if 0 <= nxt_x < m and 0 <= nxt_y < n and (nxt_x, nxt_y) not in visited:
                self.helper(board, nxt_x, nxt_y, prefix, temp, visited, res)
        visited.remove((x, y))
