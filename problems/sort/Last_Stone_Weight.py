'''
https://leetcode.com/problems/last-stone-weight/

We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.
Suppose the stones have weights x and y with x <= y. The result of this smash is:
If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new
weight y-x.
At the end, there is at most 1 stone left. Return the weight of this stone (or 0 if there
are no stones left.)

Example 1:
Input: [2,7,4,1,8,1]
Output: 1
Explanation:
We combine 7 and 8 to get 1 so the array converts to [2,4,1,1,1] then,
we combine 2 and 4 to get 2 so the array converts to [2,1,1,1] then,
we combine 2 and 1 to get 1 so the array converts to [1,1,1] then,
we combine 1 and 1 to get 0 so the array converts to [1] then that's the value of last
stone.

Note:
1 <= stones.length <= 30
1 <= stones[i] <= 1000
'''

'''
Applicable algorithm:
1. bucket sort
2. priority queue
'''

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        algorithm: bucket sort, create a bucket with size of max(stones) + 1 (because the
        max value in stones should also be included), count each stone and put to the
        corresponding bucket. Then starting from the biggest bucket, if it has
        even number of stones, they are able to cancel each other, if it has odd stones,
        find the next biggest stone and add their difference to the bucket, repeat until
        all the buckets are visited
        '''
        maxWeight = max(stones)
        buckets = [0] * (maxWeight + 1)
        for s in stones:
            buckets[s] += 1

        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i] & 0x1 == 0:
                continue

            j = i - 1
            while j > 0 and buckets[j] == 0:
                j -= 1

            if j == 0:
                return i

            buckets[j] -= 1
            buckets[i - j] += 1
        return 0
