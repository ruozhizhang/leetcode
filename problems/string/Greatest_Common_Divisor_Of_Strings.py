'''
https://leetcode.com/problems/greatest-common-divisor-of-strings/

For strings S and T, we say "T divides S" if and only if S = T + ... + T  (T concatenated
with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.

Example 1:
Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:
Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:
Input: str1 = "LEET", str2 = "CODE"
Output: ""

Note:
1 <= str1.length <= 1000
1 <= str2.length <= 1000
str1[i] and str2[i] are English uppercase letters.
'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        algorithm:
        if two strings have gcd, then the longer string must start with the shorter string,
        because both will be multiple of gcd

        1. if longer string starts with shorter string, remove the prefix (shorter string)
        from longer string, check the rest of it and shorter string recursively (these two
        will have the same gcd as the original two strings, if original two have gcd,
        because removing shorter string from longer string just changes the multiple), else
        return ''
        2. if finally one of the strings becomes empty, the other one is the answer
        '''
        if not str1 or not str2:
            return str1 if str1 else str2
        elif len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        elif str1[:len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):], str2)
        else:
            return ''
