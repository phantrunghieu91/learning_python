'''
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome that can be built with those letters.
Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:
Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:
    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        res = 0
        hadOdd = False
        for i in count:
            if count[i] % 2 == 0:
                res += count[i]
            else:
                res += count[i] - 1
                hadOdd = True
        return res + 1 if hadOdd else res
    
# Test cases
# print(Solution().longestPalindrome("abccccdd")) # 7
# print(Solution().longestPalindrome("a")) # 1
# print(Solution().longestPalindrome("cbananas")) # 5
print(Solution().longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth")) # 983