'''
https://leetcode.com/problems/multiply-strings/

Given two non-negative integers num1 and num2 represented as strings, return the
product of num1 and num2, also represented as a string.

Example 1:
Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:
Input: num1 = "123", num2 = "456"
Output: "56088"

Note:
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

'''
Approach 1
Key observation/Invariant:
1. the length of product can be m + n or m + n + 1, if it is m + n + 1, the highest digit
is the final carry
2. think about the index reversely, then index i in result comes
from two indexs of num1 and num2 which sum up to i (plus the carry which can be a reusable
variable for all digits)

Index   2   1   0
###################
        1   2   3
        4   5   6
-------------------
        7   3   8
    6   1   5
4   9   2
###################
4   3   2   1   0

Good code practice:
# remove extra preceeding characters in a string
str.lstrip('0') or '0'
# reverse a string
str[::-1]
'''

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        res = ''
        for t in range(m + n - 1):
            digit = carry
            i = 0
            while i < m:
                j = t - i
                if j < 0 or j >= n:
                    i += 1
                    continue
                digit += int(num1[i]) * int(num2[j])
                i += 1
            carry, digit = divmod(digit, 10)
            res = str(digit) + res
        if carry:
            res = str(carry) + res
        return res.lstrip('0') or '0'
