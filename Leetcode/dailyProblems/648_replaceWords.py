'''
648. Replace Words

In English, we have a concept called root, which can be followed by some other word to form another longer word - let's call this word derivative. For example, when the root "help" is followed by the word "ful", we can form a derivative "helpful".
Given a dictionary consisting of many roots and a sentence consisting of words separated by spaces, replace all the derivatives in the sentence with the root forming it. If a derivative can be replaced by more than one root, replace it with the root that has the shortest length.
Return the sentence after the replacement.

Example 1:
Input: dictionary = ["cat","bat","rat"], sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Example 2:
Input: dictionary = ["a","b","c"], sentence = "aadsfasf absbs bbab cadsfafs"
Output: "a a b c"
'''
from typing import List
class Solution:
  def replaceWords(self, dict:List[str], sentences: str) -> str:
    words = sentences.split()
    dictSet = set(dict)
    print(dictSet)
    def shortestRoot(word):
      for i in range(1, len(word)):
        if word[:i] in dictSet:
          return word[:i]
      return word
    for i in range(len(words)):
      words[i] = shortestRoot(words[i])
    return ' '.join(words)

# Test cases
print(Solution().replaceWords(["catt","cat","bat","rat"], "the cattle was rattled by the battery")) # "the cat was rat by the bat"