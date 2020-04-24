'''
https://leetcode.com/problems/restore-the-array/

A program was supposed to print an array of integers. The program forgot to print whitespaces
and the array is printed as a string of digits and all we know is that all integers in the array
were in the range [1, k] and there are no leading zeros in the array.

Given the string s and the integer k. There can be multiple ways to restore the array.

Return the number of possible array that can be printed as a string s using the mentioned program.

The number of ways could be very large so return it modulo 10^9 + 7

Example 1:
Input: s = "1000", k = 10000
Output: 1
Explanation: The only possible array is [1000]

Example 2:
Input: s = "1000", k = 10
Output: 0
Explanation: There cannot be an array that was printed this way and has all integer >= 1 and <= 10.

Example 3:
Input: s = "1317", k = 2000
Output: 8
Explanation: Possible arrays are [1317],[131,7],[13,17],[1,317],[13,1,7],[1,31,7],[1,3,17],[1,3,1,7]

Example 4:
Input: s = "2020", k = 30
Output: 1
Explanation: The only possible array is [20,20]. [2020] is invalid because 2020 > 30. [2,020] is
ivalid because 020 contains leading zeros.

Example 5:
Input: s = "1234567890", k = 90
Output: 34

Constraints:
1 <= s.length <= 10^5.
s consists of only digits and doesn't contain leading zeros.
1 <= k <= 10^9.
'''

# Bottom up
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[n] = 1
        MOD = 10 ** 9 + 7
        for i in range(n - 1, -1, -1):
            if s[i] == '0':
                continue
            for j in range(1, len(str(k)) + 1):
                if i + j > n:
                    break
                if 1 <= int(s[i:i+j]) <= k:
                    dp[i] += dp[i + j]
                    dp[i] %= MOD
        return dp[0]

# Top down
class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        return self.helper(0, s, k, {})

    def helper(self, start, s, k, cache):
        if start in cache:
            return cache[start]
        MOD = 10 ** 9 + 7
        if start == len(s):
            return 1
        if s[start] == '0':
            return 0
        res = 0
        for i in range(1, len(str(k)) + 1):
            if start + i > len(s):
                break
            if 1 <= int(s[start:start+i]) <= k:
                res += self.helper(start + i, s, k, cache)
                res %= MOD
        cache[start] = res
        return res
