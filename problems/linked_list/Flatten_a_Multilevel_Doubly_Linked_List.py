'''
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/

You are given a doubly linked list which in addition to the next and previous pointers,
it could have a child pointer, which may or may not point to a separate doubly linked list.
These child lists may have one or more children of their own, and so on,
to produce a multilevel data structure, as shown in the example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list.
You are given the head of the first level of the list.

Constraints:
Number of Nodes will not exceed 1000.
1 <= Node.val <= 10^5
'''

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return head

        s = [head]
        while s:
            cur = s.pop()
            if cur.next:
                s.append(cur.next)
            if cur.child:
                cur.next = cur.child
                cur.child.prev = cur
                s.append(cur.child)
                cur.child = None
            if not cur.next and not cur.child and s:
                cur.next = s[-1]
                s[-1].prev = cur
        return head
