# 2597. The Number of Beautiful Subsets

# You are given an array nums of positive integers and a positive integer k.
# A subset of nums is beautiful if it does not contain two integers with an absolute difference equal to k.
# Return the number of non-empty beautiful subsets of the array nums.
# A subset of nums is an array that can be obtained by deleting some (possibly none) elements from nums. Two subsets are different if and only if the chosen indices to delete are different.

# Example 1:

# Input: nums = [2,4,6], k = 2
# Output: 4
# Explanation: The beautiful subsets of the array nums are: [2], [4], [6], [2, 6].
# It can be proved that there are only 4 beautiful subsets in the array [2,4,6].

# Example 2:

# Input: nums = [1], k = 1
# Output: 1
# Explanation: The beautiful subset of the array nums is [1].
# It can be proved that there is only 1 beautiful subset in the array [1].
class Solution(object):
    def beautifulSubsetsSlow(self, nums, k):
        """
            :type nums: List[int]
            :type k: int
            :rtype: int
        """
        nums.sort()
        subsets = [[]]
        non_beautiful_subsets = []
        for num in nums:
            subsets_len = len(subsets)
            for i in range(subsets_len):
                new_subset = subsets[i] + [num]
                if len(new_subset) == 1:
                    subsets.append(new_subset)
                else:
                    flag = False
                    for sub in non_beautiful_subsets:
                        if all(n in new_subset for n in sub):
                            flag = True
                            break
                    if flag:
                        continue
                    elif abs(new_subset[-1] - new_subset[-2]) != k:
                        subsets.append(new_subset)
                    else:
                        non_beautiful_subsets.append(new_subset)

        return len(subsets[1:])

    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # from collections import defaultdict
        n = len(nums)
        nums.sort()
        dic = {}#defaultdict(list)  # key is num%k and value is a list of num/k, don't count duplicates
        fre = {}#defaultdict(int)  # frequency

        for num in nums:
            if num not in fre:
                fre[num] = 0
            fre[num] += 1

            if num % k not in dic:
                dic[num % k] = []
            if fre[num] == 1:
                dic[num % k].append(num//k)

        ans = 1
        for key in dic:
            temp = dic[key]
            # dp means number of subsets using numbers corresponding to temp
            dp = [0] * len(temp)
            # key + temp[0] * k is the original number corresponding to temp[0], fre is the count
            dp[0] = pow(2, fre[key+temp[0]*k])

            for i in range(1, len(temp)):
                dp[i] += dp[i-1]
                # i and i-1 can not be in one group
                if temp[i] == temp[i-1] + 1:
                    dp[i] += (dp[i - 2] if i >= 2 else 1) * (pow(2, fre[key + temp[i] * k]) - 1)  # Subtract the one that completely does not use temp[i]
                else:
                    fre_key = key+temp[i]*k
                    dp[i] += dp[i-1] * (pow(2, fre[fre_key]) - 1)
            ans *= dp[len(temp)-1]

        return ans - 1


# Test cases
# print(Solution().beautifulSubsets([2,4,6], 2)) # 4
# print(Solution().beautifulSubsets([1], 1)) # 1
# print(Solution().beautifulSubsets([2,4,6,8], 2)) # 7
# print(Solution().beautifulSubsets([2,4,6,8], 1)) # 15
# print(Solution().beautifulSubsets([2,4,6,8], 3)) # 15
print(Solution().beautifulSubsets([1,1,3,4], 2)) # 6
# print(Solution().beautifulSubsets([10, 4, 5, 7, 2, 1], 3))  # 23
