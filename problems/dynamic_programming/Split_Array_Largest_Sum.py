'''
https://leetcode.com/problems/split-array-largest-sum/

Given an array which consists of non-negative integers and an integer m, you can
split the array into m non-empty continuous subarrays. Write an algorithm to minimize
the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:
1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)

Examples:
Input:
nums = [7,2,5,10,8]
m = 2
Output:
18
Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
'''

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        # f[i][j] = min(max(f[i - 1][j - 1], sum[i-1:i-1]), max(f[i - 2][j - 1], sum[i-2:i-1])
        # ... max(f[1][j - 1], sum[1:i-1]))
        n = len(nums)
        f = [[float('inf')] * (m + 1) for _ in range(n + 1)]
        total = 0
        for i in range(1, n + 1):
            total += nums[i - 1]
            f[i][1] = total
        for i in range(2, n + 1):
            for j in range(2, m + 1):
                if i < j:
                    continue
                total = 0
                for k in range(i - 1, 0, -1):
                    total += nums[k]
                    f[i][j] = min(f[i][j], max(f[k][j - 1], total))
        return f[n][m]
