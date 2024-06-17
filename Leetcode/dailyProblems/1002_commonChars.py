'''
1002. Find Common Characters

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:
Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

Example 2:
Input: words = ["cool","lock","cook"]
Output: ["c","o"]

Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of lowercase English letters.
'''
from typing import List
class Solution:
  def commonChars(self, words: List[str]) -> List[str]:
    res = []
    common = [0] * 26
    for c in words[0]:
      common[ord(c) - ord('a')] += 1
    for word in words[1:]:
      count = [0] * 26
      for c in word:
        count[ord(c) - ord('a')] += 1
      for i in range(26):
        common[i] = min(common[i], count[i])
    for i in range(len(common)):
      if common[i] > 0:
        res.extend([chr(ord('a') + i)] * common[i])
    return res
  
# Test cases
# print(Solution().commonChars(["bella","label","roller"])) # ["e","l","l"]
print(Solution().commonChars(["cool","lock","cook"])) # ["c","o"]