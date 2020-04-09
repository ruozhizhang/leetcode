'''
https://leetcode.com/problems/rectangle-area/

Find the total area covered by two rectilinear rectangles in a 2D plane.
Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Example:
Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45

Note:
Assume that the total area is never beyond the maximum possible value of int.
'''

class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        x1, y1, x2, y2 = A, B, C, D
        x1_, y1_, x2_, y2_ = E, F, G, H
        res = (x2 - x1) * (y2 - y1) + (x2_ - x1_) * (y2_ - y1_)
        if x1 < x2_ and y1 < y2_ and x1_ < x2 and y1_ < y2:
            overlap = (min(x2, x2_) - max(x1, x1_)) * (min(y2, y2_) - max(y1, y1_))
            res -= overlap
        return res
