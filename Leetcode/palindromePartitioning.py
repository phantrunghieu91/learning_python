# 131. Palindrome Partitioning

# Given a string s, partition s such that every substring of the partition is a palindrome (A palindrome is a string that reads the same forward and backward). Return all possible palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]

# Constraints:
#     1 <= s.length <= 16
#     s contains only lowercase English letters.

class Solution(object):
  """
  Class representing a solution for palindrome partitioning problem.
  
  Attributes:
    None
    
  Methods:
    is_palindrome: Check if a string is a palindrome.
    partition: Partition a string into all possible palindrome substrings.
  """
  
  def is_palindrome(self, s):
    return s == s[::-1]
  
  def partition(self, s, memo={}):
    """
    Partition a string into all possible palindrome substrings.
    
    Args:
      s (str): The input string to be partitioned.
      memo (dict): A memoization dictionary to store previously computed results.
      
    Returns:
      List[List[str]]: A list of lists, where each inner list represents a partition of the input string.
    """
    if s in memo:
      return memo[s]
    
    if len(s) == 0:
      return [[]]
    
    if len(s) == 1:
      memo[s] = [[s]]
      return [[s]]
    
    res = []
    for i in range(1, len(s)+1):
      fromStartToI = s[:i]
      fromItoEnd = s[i:]
      if self.is_palindrome(fromStartToI):
        temp = self.partition(fromItoEnd, memo)
        for rest in temp:
          res.append([fromStartToI] + rest)
    
    memo[s] = res
    return res

# Test cases
print(Solution().partition("aab")) # [["a","a","b"],["aa","b"]]
# print(Solution().partition("a")) # [["a"]]
# print(Solution().partition("ab")) # [["a","b"]]
# print(Solution().partition("aabb")) # [["a","a","b","b"],["a","a","bb"],["aa","b","b"],["aa","bb"]]