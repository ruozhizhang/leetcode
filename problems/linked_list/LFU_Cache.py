'''
https://leetcode.com/problems/lfu-cache/

Design and implement a data structure for Least Frequently Used (LFU) cache. It
should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists
in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present.
When the cache reaches its capacity, it should invalidate the least frequently
used item before inserting a new item. For the purpose of this problem, when
there is a tie (i.e., two or more keys that have the same frequency), the least
recently used key would be evicted.

Note that the number of times an item is used is the number of calls to the get
and put functions for that item since it was inserted. This number is set to zero
when the item is removed.

Follow up:
Could you do both operations in O(1) time complexity?

Example:
LFUCache cache = new LFUCache( 2 /* capacity */ );
cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.get(3);       // returns 3.
cache.put(4, 4);    // evicts key 1.
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
'''

class ListNode:
    def __init__(self, key=None, value=None, freq=0, next=None):
        self.key = key
        self.value = value
        self.freq = freq
        self.next = next

class LFUCache:

    def __init__(self, capacity: int):
        # key 2 pre node
        self.cache = {}
        self.head = ListNode()
        # freq 2 tail
        self.tails = {}
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        pre = self.cache[key]
        value = pre.next.value
        freq = pre.next.freq
        tail = self.tails[freq + 1] if freq + 1 in self.tails else self.tails[freq]
        if tail == pre.next:
            if pre.freq != tail.freq:
                del self.tails[freq]
            else:
                self.tails[freq] = pre
            tail.freq += 1
            self.tails[freq + 1] = tail
            return value
        self.pop(pre)
        self.append(tail, key, value, freq + 1)
        return value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            if len(self.cache) == self.cap:
                self.pop(self.head)
            if len(self.cache) < self.cap:
                tail = self.tails[1] if 1 in self.tails else self.head
                self.append(tail, key, value, 1)
        else:
            pre = self.cache[key]
            freq = pre.next.freq
            tail = self.tails[freq + 1] if freq + 1 in self.tails else self.tails[freq]
            if tail == pre.next:
                if pre.freq != tail.freq:
                    del self.tails[freq]
                else:
                    self.tails[freq] = pre
                tail.value = value
                tail.freq += 1
                self.tails[freq + 1] = pre.next
                #self.ph('put 0')
                #print('put0 ', self.cache)
                return
            self.pop(pre)
            self.append(tail, key, value, freq + 1)

    def append(self, tail, key, value, freq):
        node = ListNode(key, value, freq)
        nxt = tail.next
        if nxt:
            self.cache[nxt.key] = node
        node.next = nxt
        tail.next = node
        self.cache[key] = tail
        self.tails[freq] = node

    def pop(self, pre):
        if not pre.next:
            return
        popped = pre.next
        nxt = popped.next
        pre.next = nxt
        if nxt:
            self.cache[nxt.key] = pre
        del self.cache[popped.key]
        if self.tails[popped.freq] == popped:
            if pre.freq != popped.freq:
                del self.tails[popped.freq]
            else:
                self.tails[popped.freq] = pre

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
