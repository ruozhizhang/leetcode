'''
https://leetcode.com/problems/remove-k-digits/

Given a non-negative integer num represented as a string, remove k digits from the number so that
the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
Example 1:

Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
Example 2:

Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200. Note that the output must not contain
leading zeroes.
Example 3:

Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing which is 0.
'''

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        '''
        algorithm: find the first k peak elements and remove them
            why peak element?
                for exmaple:
                12435
                removing 1 -> 2435, if the current digit is smaller than next one, removing it
                will make the result bigger
                removing 2 -> 1435
                removing 4 -> 1235
                removing 3 -> 1245
                removing 5 -> 1243

            why first k?
                comparing to later peak elements, first k peak elements have higher weights

            if there are less than k peak elements in num, for the rest, remove the last digits
            (these are also like peak elements if assuming the boundary is always smaller that
            digit)

        stack can be used to find all peak elements
        '''
        stack = []

        for digit in num:
            while stack and stack[-1] > digit and k:
                stack.pop()
                k -= 1
            stack.append(digit)

        while k > 0:
            stack.pop()
            k -= 1

        return ''.join(stack).lstrip('0') or '0'
