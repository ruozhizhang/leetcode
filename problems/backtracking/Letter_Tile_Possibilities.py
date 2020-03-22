'''
https://leetcode.com/problems/letter-tile-possibilities/

You have a set of tiles, where each tile has one letter tiles[i] printed on it.
Return the number of possible non-empty sequences of letters you can make.

Example 1:
Input: "AAB"
Output: 8
Explanation: The possible sequences are "A", "B", "AA", "AB", "BA", "AAB",
"ABA", "BAA".

Example 2:
Input: "AAABBC"
Output: 188

Note:
1 <= tiles.length <= 7
tiles consists of uppercase English letters.
'''

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counts = [0] * 26
        for ch in tiles:
            counts[ord(ch) - ord('A')] += 1

        res = []
        self.helper(counts, '', res)
        return len(res)

    def helper(self, counts, cur, res):
        for i in range(26):
            if counts[i] == 0:
                continue

            nxt = cur + chr(ord('A') + i)
            res.append(nxt)
            counts[i] -= 1
            self.helper(counts, nxt, res)
            counts[i] += 1
