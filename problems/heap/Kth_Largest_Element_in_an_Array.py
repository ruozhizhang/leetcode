'''
https://leetcode.com/problems/kth-largest-element-in-an-array/

Find the kth largest element in an unsorted array. Note that it is the kth largest
element in the sorted order, not the kth distinct element.

Example 1:
Input: [3,2,1,5,6,4] and k = 2
Output: 5

Example 2:
Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4

Note:
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.quickSelect(nums, 0, len(nums) - 1, k)

    def quickSelect(self, nums, l, r, k):
        if l > r:
            return None
        if l == r:
            return nums[l]

        mid = l + (r - l) // 2
        nums[mid], nums[r] = nums[r], nums[mid]
        j = l
        for i in range(l, r):
            if nums[i] >= nums[r]:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        nums[j], nums[r] = nums[r], nums[j]

        if j - l + 1 == k:
            return nums[j]
        elif j - l + 1 > k:
            return self.quickSelect(nums, l, j - 1, k)
        else:
            return self.quickSelect(nums, j + 1, r, k - j + l - 1)
