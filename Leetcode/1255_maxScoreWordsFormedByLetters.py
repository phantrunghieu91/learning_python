# 1255. Maximum Score Words Formed by Letters

# Given a list of words, list of  single letters (might be repeating) and score of every character.
# Return the maximum score of any valid set of words formed by using the given letters (words[i] cannot be used two or more times).
# It is not necessary to use all characters in letters and each letter can only be used once. Score of letters 'a', 'b', 'c', ... ,'z' is given by score[0], score[1], ... , score[25] respectively.

# Example 1:
# Input: words = ["dog","cat","dad","good"], letters = ["a","a","c","d","d","d","g","o","o"], score = [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]
# Output: 23
# Explanation:
# Score  a=1, c=9, d=5, g=3, o=2
# Given letters, we can form the words "dad" (5+1+5) and "good" (3+2+2+5) with a score of 23.
# Words "dad" and "dog" only get a score of 21.

# Example 2:
# Input: words = ["xxxz","ax","bx","cx"], letters = ["z","a","b","c","x","x","x"], score = [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10]
# Output: 27
# Explanation:
# Score  a=4, b=4, c=4, x=5, z=10
# Given letters, we can form the words "ax" (4+5), "bx" (4+5) and "cx" (4+5) with a score of 27.
# Word "xxxz" only get a score of 25.

# Example 3:
# Input: words = ["leetcode"], letters = ["l","e","t","c","o","d"], score = [0,0,1,1,1,0,0,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0]
# Output: 0
# Explanation:
# Letter "e" can only be used once.
class Solution(object):
    def subsetOf(self, arr):
        if (len(arr) == 0):
            return []
        result = [[]]
        for i in range(len(arr)):
            n = len(result)
            for j in range(n):
                result.append(result[j] + [arr[i]])
        return result

    def maxScoreWordsSlow(self, words, letters, score):
        import collections
        # count letter frequency
        if len(words) == 0 or len(letters) == 0:
            return 0
        max_score = 0
        letter_freq = {}
        score_of_words = {}

        for letter in letters:
            letter_freq[letter] = letter_freq.get(letter, 0) + 1
        # all combined words
        combined_words = self.subsetOf(words)
        for word_set in combined_words:
            letter_freq_copy = letter_freq.copy()
            temp_score = 0
            for word in word_set:
                can_word_be_formed = True
                letter_freq_minus = {}
                for letter in word:
                    if letter not in letter_freq_copy or letter_freq_copy[letter] == 0:
                        can_word_be_formed = False
                        for letter in letter_freq_minus:
                            letter_freq_copy[letter] += 1
                        break
                    if letter not in letter_freq_minus:
                        letter_freq_minus[letter] = 1
                    else:
                        letter_freq_minus[letter] += 1
                    letter_freq_copy[letter] -= 1
                if can_word_be_formed:
                    if score_of_words.get(word) != None:
                        temp_score += score_of_words[word]
                    else:
                        for letter in word:
                            temp_score += score[ord(letter) - ord('a')]
                        score_of_words[word] = temp_score
            if temp_score > max_score:
                max_score = temp_score

        return max_score
    
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        from collections import Counter

        def bckt(i, counts):
            if i == len(words): return 0
            word = Counter(words[i])
            if word == word & counts:
                curr = sum([score[ord(c) - ord("a")] * word[c] for c in word])
                return max(curr + bckt(i + 1 , counts - word), bckt(i + 1, counts))
            return bckt(i + 1, counts)

        return bckt(0, Counter(letters))

# Test case
print(Solution().maxScoreWords(["dog","cat","dad","good"], ["a","a","c","d","d","d","g","o","o"], [1,0,9,5,0,0,3,0,0,0,0,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0])) # 23
# print(Solution().maxScoreWords(["xxxz","ax","bx","cx"], ["z","a","b","c","x","x","x"], [4,4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,5,0,10])) # 27
# print(Solution().maxScoreWords(["aac", "ab", "cc", "aab"], ["a", "a", "a", "b", "c", "c"], [1, 5, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # 23
# print(Solution().maxScoreWords(["da","ac","aba","abcc","cadc"], ["a","a","a","a","b","c","c","c","d","d","d"], [3,7,9,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))  # 49
# print(Solution().maxScoreWordsSlow(["ac", "abd", "db", "ba", "dddd", "bca"], ["a", "a", "a", "b", "b", "b", "c", "c", "d", "d", "d", "d"], [6, 4, 4, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))  # 62
