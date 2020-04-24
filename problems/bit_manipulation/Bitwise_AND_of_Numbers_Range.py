'''
https://leetcode.com/problems/bitwise-and-of-numbers-range/

Given a range [m, n] where 0 <= m <= n <= 2147483647, return the bitwise AND of all
numbers in this range, inclusive.

Example 1:
Input: [5,7]
Output: 4

Example 2:
Input: [0,1]
Output: 0
'''

'''
Algorithm: if we find the first different bit in m and n, then starting from this bit
to the end, the AND result of these bits will be 0, before this bit, the AND result
will be same as their original value (i.e. the prefix of m and n)

For example: m = 10010010, n = 10010111, the first different bit is bit 2, then bit[7:3]
will be the same for all the numbers between m and n, so the corresponding bits in the
result will also be the same prefix. For bit[2:0], the AND result must be 0, because there
must be two numbers between m and n which are 10010011 and 10010100, their AND result will
be prefix + all 0s, then the whole AND result between m and n will also be prefix + all 0s

Then the problem becomes to find the prefix between m and n
Algo 1: right shift m and n until they are same (which is the prefix), record how many steps
shifted, then the result is prefix left shift the number of steps

Algo 2: turn off the rightmost bit 1 of n (by n & (n - 1)) until m >= n,
'''

# Algo 1
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        step = 0
        while m != n:
            m >>= 1
            n >>= 1
            step += 1
        return m << step

# Algo 2
class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        while m < n:
            n = n & (n - 1)
        return n
