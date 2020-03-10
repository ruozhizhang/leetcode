'''
https://leetcode.com/problems/print-immutable-linked-list-in-reverse/

You are given an immutable linked list, print out all values of each node in reverse with
the help of the following interface:

ImmutableListNode: An interface of immutable linked list, you are given the head of the
list. You need to use the following functions to access the linked list (you can't access
the ImmutableListNode directly):

ImmutableListNode.printValue(): Print value of the current node.
ImmutableListNode.getNext(): Return the next node.
The input is only given to initialize the linked list internally. You must solve this
problem without modifying the linked list. In other words, you must operate the linked list
using only the mentioned APIs.

Follow up:
Could you solve this problem in:
Constant space complexity?
Linear time complexity and less than linear space complexity?
'''

'''
Applicable algorithm:
1. O(n) time, O(n) space
2. O(n ^ 2) time, O(1) space
3. O(n) time, O(n ^ 1/2) space
'''

class Solution:
    # O(n) time, O(n) space
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        '''
        O(n) time, O(n) space algorithm: print all nodes recursively (or with a stack)
        '''
        if not head:
            return
        self.printLinkedListInReverse(head.getNext())
        head.printValue()

    # O(n ^ 2) time, O(1) space
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        '''
        O(n ^ 2) time, O(1) space algorithm: initialize tail to None, starting from head, find the node whose next is tail,
        print its value, assign it to be the new tail, repeat this process until tail becomes head
        '''
        tail = None
        while tail != head:
            cur = head
            while cur.getNext() != tail:
                cur = cur.getNext()
            cur.printValue()
            tail = cur

    # O(n) time, O(n ^ 1/2) space
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        '''
        O(n) time, O(n ^ 1/2) space algorithm:
        1. count the total number of nodes n -> O(n) time, O(1) space
        2. divide all nodes into sqrt(n) groups, get the head of each group -> O(n) time,
        O(n ^ 1/2) space
        3. recursively print each group's node value -> O(n) time, O(n ^ 1/2) space
        '''
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        numBlocks = math.ceil(math.sqrt(n))
        blockSize = math.ceil(n / numBlocks)

        heads = []
        cur = head
        for i in range(n):
            if i % blockSize == 0:
                heads.append(cur)
            cur = cur.next

        for h in heads[::-1]:
            self.helper(h, blockSize)

    def helper(self, head, size):
        if head and size:
            self.helper(head.getNext(), size - 1)
            head.printValue()
