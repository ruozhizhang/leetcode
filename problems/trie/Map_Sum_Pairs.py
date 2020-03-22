'''
https://leetcode.com/problems/map-sum-pairs/

Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer). The string
represents the key and the integer represents the value. If the key already
existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix, and you
need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
'''

class TrieNode:
    def __init__(self, value):
        self.children = {}
        self.value = value

class MapSum:
    def __init__(self):
        self.root = TrieNode(0)
        self.d = {}

    def insert(self, key: str, val: int) -> None:
        if key in self.d:
            temp = self.d[key]
            self.d[key] = val
            val -= temp
        else:
            self.d[key] = val

        cur = self.root
        for ch in key:
            if ch not in cur.children:
                cur.children[ch] = TrieNode(0)
            cur = cur.children[ch]
            cur.value += val

    def sum(self, prefix: str) -> int:
        cur = self.root
        for ch in prefix:
            if ch not in cur.children:
                return 0
            cur = cur.children[ch]
        return cur.value

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
