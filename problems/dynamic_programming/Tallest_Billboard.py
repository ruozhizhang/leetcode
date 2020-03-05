'''
https://leetcode.com/problems/tallest-billboard/

You are installing a billboard and want it to have the
largest height.  The billboard will have two steel
supports, one on each side.  Each steel support must be an
equal height.

You have a collection of rods which can be welded
together.  For example, if you have rods of lengths 1, 2,
and 3, you can weld them together to make a support of
length 6.

Return the largest possible height of your billboard
installation.  If you cannot support the billboard, return
0.

Example 1:
Input: [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6},
which have the same sum = 6.

Example 2:
Input: [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and
{4,6}, which have the same sum = 10.

Example 3:
Input: [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we
return 0.

Note:
0 <= rods.length <= 20
1 <= rods[i] <= 1000
The sum of rods is at most 5000.
'''

'''
Thinking process: consider this problem as choosing -1, 0,
1 to multiply with each number, the goal is to get the
biggest positive sum when the final sum is 0 (which means
the sum of numbers chosen to multiply with 1 equals the sum
of number chosen to multiply with -1).
In this way the problem becomes similar to knapsack problem

Algorithm: use a dict preSum, whose key is the total sum we
have met so far, and value is the corresponding positive
sum. With each rod number, it can produce the new total sum
as preSum + rod, preSum - rod or preSum, for each possible
total sum, maximize the corresponding positive sum. Finally
return the positive sum for total sum 0

Initial value: preSum[0] = 0. Initially there is no rod
number so both total sum and positive sum is 0
'''

from collections import defaultdict
class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        preSum = {0: 0}

        for l in rods:
            curSum = defaultdict(int)
            for s in preSum:
                curSum[s + l] = max(preSum[s] + l, curSum[s + l])
                curSum[s - l] = max(preSum[s], curSum[s - l])
                curSum[s] = max(preSum[s], curSum[s])
            preSum = curSum

        return preSum[0]
