'''
https://leetcode.com/problems/lru-cache/

Design and implement a data structure for Least Recently Used (LRU) cache.
It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reached its capacity, it should invalidate the least recently
used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
LRUCache cache = new LRUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

class ListNode:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.head = ListNode()
        self.tail = self.head
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        pre = self.cache[key]
        value = pre.next.value
        self.pop(pre)
        self.append(key, value)
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.cap:
                self.pop(self.head)
            self.append(key, value)
        else:
            pre = self.cache[key]
            self.pop(pre)
            self.append(key, value)

    def pop(self, pre):
        if not pre.next:
            return
        popped = pre.next
        del self.cache[popped.key]
        pre.next = popped.next
        if popped.next:
            self.cache[popped.next.key] = pre
        if self.tail == popped:
            self.tail = pre

    def append(self, key, value):
        node = ListNode(key, value)
        self.tail.next = node
        self.cache[key] = self.tail
        self.tail = node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
