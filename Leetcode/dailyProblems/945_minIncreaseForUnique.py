'''
945. Minimum Increment to Make Array Unique


You are given an integer array nums. In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.
Return the minimum number of moves to make every value in nums unique.
The test cases are generated so that the answer fits in a 32-bit integer.

Example 1:
Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].

Example 2:
Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
'''
from typing import List
class Solution:
  def minIncrementForUnique(self, nums: List[int]) -> int:
    N = len(nums)
    if N == 0:
      return 0
    res = 0
    nums.sort()
    for i in range(1, N):
      if nums[i] <= nums[i - 1]:
        diff = nums[i - 1] - nums[i]
        res += diff + 1
        nums[i] += diff + 1
      
    return res
  
# test cases
# print(Solution().minIncrementForUnique([1,2,2]))  # 1
print(Solution().minIncrementForUnique([3,2,1,2,1,7]))  # 6 
