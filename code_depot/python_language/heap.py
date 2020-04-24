'''
import heapq
heap invariant: heap[k] <= heap[2 * k + 1] and heap[k] <= heap[2 * k + 2], index
                starts with 0, heap.sort() still keeps the invariant
1. create heap
    1) use an empty list and add elements gradually
    2) use heapq.heapify() on a populated list
2. min item: heap[0]
3. heapq.heappush(q, item), heapq.heappop(q)
4. heapq.heappushpop(q, item) -> push then pop
5. heapq.heapreplace(q, item) -> pop then push, the value returned may be larger
   than the one added

Application:
1. heapq.merge(*iterable, key=None, reverse=False) -> merge sorted inputs into
   a single output
   e.g. merge k sorted arrays
   (https://www.lintcode.com/problem/merge-k-sorted-arrays/description)
   import heapq
   class Solution:
    """
    @param arrays: k sorted integer arrays
    @return: a sorted array
    """
    def mergekSortedArrays(self, arrays):
        return list(heapq.merge(*arrays))

2. heapq.nlargest(n, iterable, key=None) -> returns a list with n largest items
   from iterable
   equivalent to: sorted(iterable, key=key, reverse=True)[:n]
3. heapq.nsmallest(n, iterable, key=None) -> returns a list with n smallest items
   from iterable
   equivalent to: sorted(iterable, key=key)[:n]
Note: 1) these two functions work better on smaller value of n, if n is large, sorted()
      fucntion is more efficient
      2) if n == 1, min() and max() are more efficient
      3) if repeated usage is needed, turn iterable into an actual heap
'''
