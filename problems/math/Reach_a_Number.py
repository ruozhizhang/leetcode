'''
https://leetcode.com/problems/reach-a-number/submissions/

You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n
steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
Note:
target will be a non-zero integer in the range [-10^9, 10^9].
'''

class Solution:
    def reachNumber(self, target: int) -> int:
        '''
        1. make target positive as the number of steps to reach positive target will be the same as
        negative target due to symmetry
        2. make several right moves until the sum of moves is greater or equal to target
        3. calculate the diff between sum and target, if it is an even number, return current step
            why the current step is the answer?
            because if we change any move i from right to left, the difference in the sum will be
            2 * i, and since we have all the moves from 1 to n available, we can always find
            (sum - target) // 2 as one of the moves, then just change it from right to left, we can
            get the needed moves including direction
        4. if the diff is odd, continue to add right moves until it becomes even, then return the
        current step
        '''
        target = abs(target)
        distance = 0
        step = 0
        while distance < target:
            step += 1
            distance += step

        if (distance - target) & 0x1 == 0:
            return step

        while (distance - target) & 0x1 == 1:
            step += 1
            distance += step

        return step
