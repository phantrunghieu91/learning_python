# Largest Substring Between Two Equal Characters

# Given a string s, return the length of the longest substring between two equal characters, excluding the two characters. If there is no such substring return -1.
# A substring is a contiguous sequence of characters within a string.

# Example 1:
# Input: s = "aa"
# Output: 0
# Explanation: The optimal substring here is an empty substring between the two 'a's.

# Example 2:
# Input: s = "abca"
# Output: 2
# Explanation: The optimal substring here is "bc".

# Example 3:
# Input: s = "cbzxy"
# Output: -1
# Explanation: There are no characters that appear twice in s.

# Constraints:
#     1 <= s.length <= 300
#     s contains only lowercase English letters.

class Solution(object):
  def maxLengthBetweenEqualCharacters(self, s):
    if(len(s) == 0): return - 1
    substr_len = {}
    for char in s:
      count = s.count(char)
      if count == 1:
        continue
      else:
        substr_len[char] = s.rindex(char) - s.index(char) - 1
    if len(substr_len) == 0:
      return -1
    return max(substr_len.values())
  
# Test case
print(Solution().maxLengthBetweenEqualCharacters("aa")) # 0
print(Solution().maxLengthBetweenEqualCharacters("abca")) # 2
print(Solution().maxLengthBetweenEqualCharacters("cbzxy")) # -1
print(Solution().maxLengthBetweenEqualCharacters("cbzxyc")) # 4