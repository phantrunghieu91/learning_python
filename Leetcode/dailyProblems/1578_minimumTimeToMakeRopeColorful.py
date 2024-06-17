# 1578. Minimum Time to Make Rope Colorful

# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.
# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.
# Return the minimum time Bob needs to make the rope colorful.

# Example 1:
# Input: colors = "abaac", neededTime = [1,2,3,4,5]
# Output: 3
# Explanation: In the above image, 'a' is blue, 'b' is red, and 'c' is green.
# Bob can remove the blue balloon at index 2. This takes 3 seconds.
# There are no longer two consecutive balloons of the same color. Total time = 3.

# Example 2:
# Input: colors = "aabaa", neededTime = [1,2,3,4,1]
# Output: 2
# Explanation: Bob will remove the balloons at indices 0 and 4. Each balloons takes 1 second to remove.
# There are no longer two consecutive balloons of the same color. Total time = 1 + 1 = 2.

class Solution(object):
  def minCost(self, colors, neededTime):
    """
        :type colors: str
        :type neededTime: List[int]
        :rtype: int
    """
    # convert colors string into list
    colors = list(colors)
    sum = 0
    if(len(colors) == 1):
      return 0
    
    i = 1

    while i < len(colors):
      if colors[i] == colors[i-1]:
        if neededTime[i] < neededTime[i-1]:
          sum += neededTime.pop(i)
          colors.pop(i)
        else:
          sum += neededTime.pop(i-1)
          colors.pop(i-1)
      else:
        i += 1
    return sum
  
# Test case
# print(Solution().minCost("abaac", [1,2,3,4,5]))  # 3
# print(Solution().minCost("aabaa", [1,2,3,4,1]))  # 2
# print(Solution().minCost("a", [1]))  # 0
# print(Solution().minCost("aa", [1, 2]))  # 1
# print(Solution().minCost("aa", [2, 1]))  # 1
# print(Solution().minCost("ab", [1, 2]))  # 0
print(Solution().minCost("aaabbb", [4,9,3,8,8,9]))  # 23
