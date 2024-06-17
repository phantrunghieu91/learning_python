'''
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:
Input: nums = [], target = 0
Output: [-1,-1]

Constraints:
    0 <= nums.length <= 105
    -109 <= nums[i] <= 109
    nums is a non-decreasing array.
    -109 <= target <= 109
'''
from typing import List
class Solution:
  def searchRange(self, nums: List[int], target: int) -> List[int]:
    if not nums:
      return [-1, -1]
    def findFirst(nums: List[int], target: int) -> int:
      left, right = 0, len(nums) - 1
      while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
          left = mid
        else:
          right = mid
      if nums[left] == target:
        return left
      if nums[right] == target:
        return right
      return -1
    def findLast(nums: List[int], target: int) -> int:
      left, right = 0, len(nums) - 1
      while left + 1 < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
          if nums[mid - 1] == target:
            left = mid - 1
          else:
            left = mid
        else:
          if nums[mid + 1] == target:
            left = mid
          else:
            right = mid
      if nums[right] == target:
        return right
      if nums[left] == target:
        return left
      return -1
    return [findFirst(nums, target), findLast(nums, target)]

# Test case
print(Solution().searchRange([2,4,5,6,6,8,8], 6)) # [3,4]
