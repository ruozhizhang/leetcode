'''
https://leetcode.com/problems/next-closest-time/

Given a time represented in the format "HH:MM", form the next closest time by reusing
the current digits. There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid. For example, "01:34", "12:09"
are all valid. "1:34", "12:9" are all invalid.

Example 1:
Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39, which
occurs 5 minutes later.  It is not 19:33, because this occurs 23 hours and 59 minutes later.

Example 2:
Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22. It may
be assumed that the returned time is next day's time since it is smaller than the input
time numerically.
'''

class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = sorted(set(time.replace(':', '')))
        l = [a + b for a in digits for b in digits]
        hrs, mins = time.split(':')
        # try to find the next bigger minutes
        i = l.index(mins)
        if i + 1 < len(l) and l[i + 1] <= '59':
            return hrs + ':' + l[i + 1]

        # try to find the next bigger hours, minutes need to be the minimum possible value
        i = l.index(hrs)
        if i + 1 < len(l) and l[i + 1] <= '23':
            return l[i + 1] + ':' + l[0]

        # return the minimum possible time that can be made
        return l[0] + ':' + l[0]
