# You have n dice, and each dice has k faces numbered from 1 to k.
# Given three integers n, k, and target, return the number of possible ways (out of the kn total ways) to roll the dice, so the sum of the face-up numbers equals target.
# Example 1:
# Input: n = 1, k = 6, target = 3
# Output: 1
# Explanation: You throw one die with 6 faces.
# There is only one way to get a sum of 3.
# Example 2:
# Input: n = 2, k = 6, target = 7
# Output: 6
# Explanation: You throw two dice, each with 6 faces.
# There are 6 ways to get a sum of 7: 1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
# Example 3:
# Input: n = 30, k = 30, target = 500
# Output: 222616187
# Explanation: The answer must be returned modulo 109 + 7.

class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
          :type n: int
          :type k: int
          :type target: int
          :rtype: int
        """
        MOD = 10**9 + 7
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
                for j in range(1, target + 1):
                    for l in range(1, k + 1):
                        if j - l >= 0:
                            dp[i][j] = (dp[i][j] + dp[i - 1][j - l]) % MOD
                        else: 
                            break
        print(dp)
        return dp[n][target]


# Test case
# print(Solution().numRollsToTarget(1, 6, 3))  # 1
# print(Solution().numRollsToTarget(2, 6, 7))  # 6
# print(Solution().numRollsToTarget(30, 30, 500))  # 222616187
# print(Solution().numRollsToTarget(1, 2, 3))  # 0
# print(Solution().numRollsToTarget(2, 5, 10))  # 1
# print(Solution().numRollsToTarget(2, 5, 4))  # 0
print(Solution().numRollsToTarget(3, 6, 7))  # 15
