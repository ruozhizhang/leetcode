'''
https://leetcode.com/problems/single-number-ii/

Given a non-empty array of integers, every element appears three times except
for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it
without using extra memory?

Example 1:
Input: [2,2,3,2]
Output: 3

Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for i in range(32):
            bit = 0
            for num in nums:
                if (num >> i) & 0x1:
                    bit += 1
            bit %= 3

            # if the number is negative
            if i == 31 and bit:
                res -= 1 << 31
            else:
                res |= bit << i
        return res
