'''
https://leetcode.com/problems/plus-one/

Given a non-empty array of digits representing a non-negative integer, plus one
to the integer.

The digits are stored such that the most significant digit is at the head of the
list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number
0 itself.

Example 1:
Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:
Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

'''
Approach 1, O(1) space
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i, d in enumerate(digits[::-1]):
            d += carry
            carry, digits[i] = divmod(d, 10)
        if carry:
            digits.append(carry)
        return digits[::-1]

'''
Approach 2
'''

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = int(''.join([str(d) for d in digits])) + 1
        res = []
        while num:
            res.append(num % 10)
            num //= 10
        return reversed(res)
