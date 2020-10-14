'''
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended/

Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts
at startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. Notice
that you can only attend one event at any time d.

Return the maximum number of events you can attend.

Example 1:
Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.

Example 2:
Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4

Example 3:
Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4

Example 4:
Input: events = [[1,100000]]
Output: 1

Example 5:
Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
Output: 7

Constraints:
1 <= events.length <= 105
events[i].length == 2
1 <= startDayi <= endDayi <= 105
'''

import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        # heap stores all started but not ended events
        heap = []
        # sort all events reversely so we can use it similarly as a queue, popping out values from the beginning
        events.sort(reverse=True)
        # day is the current day we care about
        day = 0
        res = 0

        while events or heap:
            # if currently there is no event ongoing, we can just skip current days until the next event starts
            if not heap:
                day = events[-1][0]

            # record the ending day of each started event, so we can exclude the outdated events on each day
            while events and events[-1][0] <= day:
                heapq.heappush(heap, events.pop()[1])

            # greedily attend the event that ends earlist to leave more time for later event
            heapq.heappop(heap)
            res += 1
            day += 1

            # remove finished events as of current day
            while heap and heap[0] < day:
                heapq.heappop(heap)

        return res
