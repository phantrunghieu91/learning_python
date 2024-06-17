'''
974. Subarray Sums Divisible by K

Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.
A subarray is a contiguous part of an array.

Example 1:
Input: nums = [4,5,0,-2,-3,1], k = 5
Output: 7
Explanation: There are 7 subarrays with a sum divisible by k = 5:
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]

Example 2:
Input: nums = [5], k = 9
Output: 0
'''
from typing import List
class Solution:
  def subarraysDivByK(self, nums: List[int], k: int) -> int:
    prefix_mod = 0
    mod_seen = {0: 1}
    count = 0

    for i in range(len(nums)):
      prefix_mod = (prefix_mod + nums[i]) % k

      if prefix_mod in mod_seen:
        count += mod_seen[prefix_mod]
        mod_seen[prefix_mod] += 1
      else:
        mod_seen[prefix_mod] = 1

    return count
  
# test cases
print(Solution().subarraysDivByK([4,5,0,-2,-3,1], 5))  # 7
print(Solution().subarraysDivByK([5], 9))  # 0
print(Solution().subarraysDivByK([1,2,3,4,5], 5))  # 7