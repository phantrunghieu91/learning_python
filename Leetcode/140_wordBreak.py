# 140. Word Break II

# Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.

# Example 1:
# Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
# Output: ["cats and dog","cat sand dog"]

# Example 2:
# Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
# Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
# Explanation: Note that you are allowed to reuse a dictionary word.

# Example 3:
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: []
class Solution(object):
  def wordBreak(self, s, wordDict):
    if len(s) == 0:
      return []
    
    memo = {}
    def dfs(i):
      if i in memo:
        return memo[i]
      if i == len(s):
        return [""]
      result = []
      for word in wordDict:
        if s[i:].startswith(word):
          rest = dfs(i + len(word))
          for r in rest:
            result.append(word + (" " + r if r else ""))
      memo[i] = result
      return result
    return dfs(0)

# Test cases
print(Solution().wordBreak("catsanddog", ["cat","cats","and","sand","dog"])) # ["cats and dog","cat sand dog"]  