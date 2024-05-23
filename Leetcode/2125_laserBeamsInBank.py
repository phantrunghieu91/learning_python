# 2125. Number of Laser Beams in a Bank
# Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.
# There is one laser beam between any two security devices if both conditions are met:
#     The two devices are located on two different rows: r1 and r2, where r1 < r2.
#     For each row i where r1 < i < r2, there are no security devices in the ith row.
# Laser beams are independent, i.e., one beam does not interfere nor join with another.
# Return the total number of laser beams in the bank.

# Example 1:
# Input: bank = ["01","10"]
# Output: 1
# Explanation: There is one laser beam that connects the security devices at bank[0][1] and bank[1][0].

# Example 2:
# Input: bank = ["011001","000000","010100","001000"]
# Output: 8
# Explanation: Between each of the following device pairs, there is one beam. In total, there are 8 beams:
#  * bank[0][1] -- bank[2][1]
#  * bank[0][1] -- bank[2][3]
#  * bank[0][2] -- bank[2][1]
#  * bank[0][2] -- bank[2][3]
#  * bank[0][5] -- bank[2][1]
#  * bank[0][5] -- bank[2][3]
#  * bank[2][1] -- bank[3][2]
#  * bank[2][3] -- bank[3][2]
# Note that there is no beam between any device on the 0th row with any on the 3rd row.
# This is because the 2nd row contains security devices, which breaks the second condition.
class Solution(object):
  def numberOfBeams(self, bank):
    devices_per_row = [row.count('1') for row in bank]
    beams = 0
    for i in range(len(bank)):
      for j in range(i+1, len(bank)):
        if(j - 1 == i):
          if devices_per_row[i] > 0 and devices_per_row[j] > 0:
            beams += devices_per_row[i] * devices_per_row[j]
            break       
        elif(j - 1 > i):
          if devices_per_row[i] > 0 and devices_per_row[j] > 0 and devices_per_row[j-1] == 0:
            beams += devices_per_row[i] * devices_per_row[j]
            break
    return beams

# Test case
# print(Solution().numberOfBeams(["011001","000000","010100","001000"]))  # 8
print(Solution().numberOfBeams(["0000111","1000000","0000000","0010000","0001101","1111111"]))  # 28