'''1442. Count Triplets That Can Form Two Arrays of Equal XOR

Given an array of integers arr.
We want to select three indices i, j and k where (0 <= i < j <= k < arr.length).
Let's define a and b as follows:
    a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]
    b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]
Note that ^ denotes the bitwise-xor operation.
Return the number of triplets (i, j and k) Where a == b.

Example 1:
Input: arr = [2,3,1,6,7]
Output: 4
Explanation: The triplets are (0,1,2), (0,2,2), (2,3,4) and (2,4,4)

Example 2:
Input: arr = [1,1,1,1,1]
Output: 10
'''
from typing import List
class Solution:
  def countTripletsSlow(self, arr: List[int]) -> int:
    res = 0
    n = len(arr)
    for i in range(n - 1):
      xor_A = 0
      for j in range(i+1, n):
        xor_A = xor_A ^ arr[j-1]
        xor_B = 0
        for k in range(j, n):
          xor_B = xor_B ^ arr[k]
          if xor_A == xor_B:
            res += 1
    return res
  def countTriplets(self, arr: List[int]) -> int:
    res = 0
    copy = [0] + arr    
    for i in range(1, len(copy)):
      copy[i] ^= copy[i-1]
    for start in range(len(copy)):
      for end in range(start+1, len(copy)):
        if copy[start] == copy[end]:
          res += end - start - 1
    return res

# Test cases
# print(Solution().countTripletsSlow([2,3,1,6,7])) # 4
print(Solution().countTriplets([2,3,1,6,7])) # 4