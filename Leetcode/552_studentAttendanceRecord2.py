# 552. Student Attendance Record II

# An attendance record for a student can be represented as a string where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:
#     'A': Absent.
#     'L': Late.
#     'P': Present.
# Any student is eligible for an attendance award if they meet both of the following criteria:
#     The student was absent ('A') for strictly fewer than 2 days total.
#     The student was never late ('L') for 3 or more consecutive days.
# Given an integer n, return the number of possible attendance records of length n that make a student eligible for an attendance award. The answer may be very large, so return it modulo 109 + 7.

# Example 1:
# Input: n = 2
# Output: 8
# Explanation: There are 8 records with length 2 that are eligible for an award:
# "PP", "AP", "PA", "LP", "PL", "AL", "LA", "LL"
# Only "AA" is not eligible because there are 2 absences (there need to be fewer than 2).

# Example 2:
# Input: n = 1
# Output: 3

# Example 3:
# Input: n = 10101
# Output: 183236316


from collections import defaultdict
class Solution:
  def checkRecord(self, n: int) -> int:
    MOD = 10**9 + 7

    if n == 1:
      return 3

    temp = {
      (0,0): 1, (0,1): 1, (0,2): 0,
      (1,0): 1, (1,1): 0, (1,2): 0 
    }
    for _ in range(n - 1):
      res = defaultdict(int)

      # Choose P
      res[(0,0)] = ( (temp[(0,0)] + temp[(0,1)]) % MOD + temp[(0,2)]) % MOD
      res[(1,0)] = ( (temp[(1,0)] + temp[(1,1)]) % MOD + temp[(1,2)]) % MOD

      # Choose L
      res[(0,1)] = temp[(0,0)]
      res[(1,1)] = temp[(1,0)]
      res[(0,2)] = temp[(0,1)]
      res[(1,2)] = temp[(1,1)]

      # Choose A
      res[(1,0)] = ( res[(1,0)] + ((temp[(0,0)] + temp[(0,1)]) % MOD + temp[(0,2)]) % MOD ) % MOD

      temp = res
    return sum(temp.values()) % MOD

    cache = {}
    def count(num: int) -> dict:
      if num == 1:
        # (A, L)
        return { 
          (0,0): 1, (0,1): 1, (0,2): 0,
          (1,0): 1, (1,1): 0, (1,2): 0 
        }
      if num in cache:
        return cache[num]
      temp = count(n-1)
      res = defaultdict(int)

      # Choose P
      res[(0,0)] = ( (temp[(0,0)] + temp[(0,1)]) % MOD + temp[(0,2)]) % MOD
      res[(1,0)] = ( (temp[(1,0)] + temp[(1,1)]) % MOD + temp[(1,2)]) % MOD

      # Choose L
      res[(0,1)] = temp[(0,0)]
      res[(1,1)] = temp[(1,0)]
      res[(0,2)] = temp[(0,1)]
      res[(1,2)] = temp[(1,1)]

      # Choose A
      res[(1,0)] = ( res[(1,0)] + ((temp[(0,0)] + temp[(0,1)]) % MOD + temp[(0,2)]) % MOD ) % MOD
      cache[num] = res
      return res
    return sum(count(n).values()) % MOD

# Test case
# print(Solution().checkRecord(2)) # Expected 8
# print(Solution().checkRecord(1)) # Expected 3
# print(Solution().checkRecord(3)) # Expected 19
# print(Solution().checkRecord(4)) # Expected 43
print(Solution().checkRecord(10101) == 183236316) # Expected 183236316