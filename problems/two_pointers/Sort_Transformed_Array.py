'''
https://leetcode.com/problems/sort-transformed-array/

Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic
function of the form f(x) = ax2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example 1:
Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]

Example 2:
Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
'''

class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        n = len(nums)
        if a == 0 and b == 0:
            return [c] * n

        res = [0] * n
        i, j = 0, n - 1
        k, d = (j, 1) if a > 0 else (i, -1)
        while i <= j:
            ni = a * nums[i] ** 2 + b * nums[i] + c
            nj = a * nums[j] ** 2 + b * nums[j] + c
            if ni * d >= nj * d:
                res[k] = ni
                i += 1
            else:
                res[k] = nj
                j -= 1
            k -= d
        return res
