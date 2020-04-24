'''
https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

Given the number k, return the minimum number of Fibonacci numbers whose sum is equal to k,
whether a Fibonacci number could be used multiple times.

The Fibonacci numbers are defined as:
F1 = 1
F2 = 1
Fn = Fn-1 + Fn-2 , for n > 2.
It is guaranteed that for the given constraints we can always find such fibonacci numbers that sum k.

Example 1:
Input: k = 7
Output: 2
Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ...
For k = 7 we can use 2 + 5 = 7.

Example 2:
Input: k = 10
Output: 2
Explanation: For k = 10 we can use 2 + 8 = 10.

Example 3:
Input: k = 19
Output: 3
Explanation: For k = 19 we can use 1 + 5 + 13 = 19.

Constraints:
1 <= k <= 10^9
'''

class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        pre2 = pre1 = 1
        while pre1 < k:
            pre2, pre1 = pre1, pre2 + pre1
        res = 0
        while k > 0:
            if pre1 <= k:
                k -= pre1
                res += 1
            pre2, pre1 = pre1 - pre2, pre2
        return res
