'''
1404. Number of Steps to Reduce a Number in Binary Representation to One

Given the binary representation of an integer as a string s, return the number of steps to reduce it to 1 under the following rules:
    If the current number is even, you have to divide it by 2.
    If the current number is odd, you have to add 1 to it.
It is guaranteed that you can always reach one for all test cases.

Example 1:
Input: s = "1101"
Output: 6
Explanation: "1101" corressponds to number 13 in their decimal representation.
Step 1) 13 is odd, add 1 and obtain 14. 
Step 2) 14 is even, divide by 2 and obtain 7.
Step 3) 7 is odd, add 1 and obtain 8.
Step 4) 8 is even, divide by 2 and obtain 4.  
Step 5) 4 is even, divide by 2 and obtain 2. 
Step 6) 2 is even, divide by 2 and obtain 1.  

Example 2:
Input: s = "10"
Output: 1
Explanation: "10" corressponds to number 2 in their decimal representation.
Step 1) 2 is even, divide by 2 and obtain 1.  

Example 3:
Input: s = "1"
Output: 0
'''
class Solution:
  def numSteps(self, s: str) -> int:
    if s == '1':
      return 0
    def binary_addition(bin1: str, bin2: str) -> str:
      max_len = max(len(bin1), len(bin2))
    
      # Normalize lengths
      bin1 = bin1.zfill(max_len)
      bin2 = bin2.zfill(max_len)
      
      result = ''
      carry = 0
      
      # Traverse the strings from the rightmost end
      for i in range(max_len - 1, -1, -1):
          bit1 = int(bin1[i])
          bit2 = int(bin2[i])
          
          # Sum the bits with the carry
          total = bit1 + bit2 + carry
          result = str(total % 2) + result
          carry = total // 2
      
      if carry:
          result = '1' + result
      
      return result
    
    def binary_subtraction(bin1, bin2):
      max_len = max(len(bin1), len(bin2))
      
      # Normalize lengths
      bin1 = bin1.zfill(max_len)
      bin2 = bin2.zfill(max_len)
      
      result = ''
      borrow = 0
      
      for i in range(max_len - 1, -1, -1):
          bit1 = int(bin1[i])
          bit2 = int(bin2[i])
          
          # Adjust bit1 for any borrow
          bit1 -= borrow
          if bit1 < bit2:
              bit1 += 2
              borrow = 1
          else:
              borrow = 0
          
          result = str(bit1 - bit2) + result
      
      # Remove leading zeros
      result = result.lstrip('0')
      return result if result else '0'
    
    def binary_division(dividend, divisor):
      # Edge case for division by zero
      if divisor == '0':
          raise ValueError("Division by zero is not allowed.")
      
      dividend_len = len(dividend)
      divisor_len = len(divisor)
      
      # Initialize the quotient
      quotient = ''
      remainder = dividend[:divisor_len - 1]  # Initially consider part of the dividend equal to the length of the divisor minus one
      
      for i in range(divisor_len - 1, dividend_len):
          # Bring down the next bit
          remainder += dividend[i]
          
          if int(remainder, 2) >= int(divisor, 2):
              # Subtract divisor from current remainder
              remainder = binary_subtraction(remainder, divisor)
              quotient += '1'
          else:
              quotient += '0'
          
          # Remove leading zeros from remainder
          remainder = remainder.lstrip('0') or '0'
      
      return quotient.lstrip('0') or '0', remainder.lstrip('0') or '0'
    steps = 0
    while s != '1':
      if s[-1] == '0':
        s = binary_division(s, '10')[0]
      else:
        s = binary_addition(s, '1')
      steps += 1
    return steps
      
  
# test the solution
sol = Solution()
# print(sol.numSteps("1101")) # 6
print(sol.numSteps("11001")) # 8
# print(sol.numSteps("10")) # 1
# print(sol.numSteps("1")) # 0