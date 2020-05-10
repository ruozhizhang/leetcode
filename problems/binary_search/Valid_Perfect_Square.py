'''
Given a positive integer num, write a function which returns True if num is a perfect
square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true

Example 2:
Input: 14
Output: false
'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        while l + 1 < r:
            mid = l + (r - l) // 2
            if mid ** 2 == num:
                return True
            elif mid ** 2 < num:
                l = mid
            else:
                r = mid
        if l ** 2 == num or r ** 2 == num:
            return True
        return False
