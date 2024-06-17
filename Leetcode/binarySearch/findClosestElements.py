'''
  Find K Closest Elements
  Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
An integer a is closer to x than an integer b if:
    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b

Example 1:
Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]

Example 2:
Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:

    1 <= k <= arr.length
    1 <= arr.length <= 104
    arr is sorted in ascending order.
    -104 <= arr[i], x <= 104
'''
from typing import List
class Solution:
  def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
    left, right = 0, len(arr) - 1
    while left + 1 < right:
      mid = left + (right - left) // 2
      if arr[mid] < x:
        left = mid
      else:
        right = mid
    res = []
    while len(res) < k:
      if left < 0:
        res.append(arr[right])
        right += 1
      elif right >= len(arr):
        res.append(arr[left])
        left -= 1
      elif abs(arr[left] - x) <= abs(arr[right] - x):
        res.append(arr[left])
        left -= 1
      else:
        res.append(arr[right])
        right += 1
    res.sort()
    return res
  def findClosestElementsFaster(self, arr: List[int], k: int, x: int) -> List[int]:
        # Initialize binary search bounds
        left = 0
        right = len(arr) - k
        
        # Binary search against the criteria described
        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]

# Test cases
# print(Solution().findClosestElementsFaster([1,2,3,4,5], 4, 3)) # [1,2,3,4]
# print(Solution().findClosestElements([1,2,3,4,5], 4, -1)) # [1,2,3,4]
print(Solution().findClosestElementsFaster([1,2,3,4,5], 4, 4)) # [1,2,3,4]
# print(Solution().findClosestElements([1,2,3,4,5], 4, 5)) # [2,3,4,5]