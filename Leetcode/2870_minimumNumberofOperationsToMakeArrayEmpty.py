# 2870. Minimum Number of Operations to Make Array Empty

# You are given a 0-indexed array nums consisting of positive integers.
# There are two types of operations that you can apply on the array any number of times:
#     Choose two elements with equal values and delete them from the array.
#     Choose three elements with equal values and delete them from the array.
# Return the minimum number of operations required to make the array empty, or -1 if it is not possible.

# Example 1:
# Input: nums = [2,3,3,2,2,4,2,3,4]
# Output: 4
# Explanation: We can apply the following operations to make the array empty:
# - Apply the first operation on the elements at indices 0 and 3. The resulting array is nums = [3,3,2,4,2,3,4].
# - Apply the first operation on the elements at indices 2 and 4. The resulting array is nums = [3,3,4,3,4].
# - Apply the second operation on the elements at indices 0, 1, and 3. The resulting array is nums = [4,4].
# - Apply the first operation on the elements at indices 0 and 1. The resulting array is nums = [].
# It can be shown that we cannot make the array empty in less than 4 operations.

# Example 2:
# Input: nums = [2,1,2,2,3,3]
# Output: -1
# Explanation: It is impossible to empty the array.

class Solution(object):
  def minOperationsSlow(self, nums):
    if(len(nums) < 2):
      return -1
    frequency = {}
    operations = {}
    for num in nums:
      if num in frequency:
        frequency[num] += 1
      else:
        frequency[num] = 1
        operations[num] = 0
    
    while len(frequency) > 0:
      i = 0
      key = list(frequency.keys())[i]
      if(frequency[key] == 0):
        i += 1
        continue
      if(frequency[key] == 1):
        return -1
      if frequency[key] == 2:
        operations[key] += 1
        del frequency[key]
        continue
      if frequency[key] % 3 == 0:
        operations[key] += frequency[key] // 3
        del frequency[key]
      elif frequency[key] % 3 != 0:
        operation = frequency[key] // 3
        if frequency[key] % 3 == 2:
          temp = frequency[key] - operation * 3
          operations[key] += operation + temp // 2
          del frequency[key]
          continue
        else:
          if operation == 1 and frequency[key] == 4:
            operations[key] += 2
            del frequency[key]
          else:
            operations[key] += operation - 1
            frequency[key] -= (operation - 1) * 3

    return sum(operations.values())
  def minOperations(self, nums):
    fre = {}
    for num in nums:
      if num in fre:
        fre[num] += 1
      else:
        fre[num] = 1
    operations = 0
    for key in fre:
      if fre[key] == 1:
        return -1
      else:
        operations += fre[key] // 3 + (fre[key] % 3 != 0)
    return operations

# Test case
# print(Solution().minOperations([2,3,3,2,2,4,2,3,4]))  # 4
print(Solution().minOperations([14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]))  # 7
print(Solution().minOperations([13,7,13,7,13,7,13,13,7]))  # -1