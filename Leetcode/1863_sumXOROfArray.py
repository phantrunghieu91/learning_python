# The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.
# For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
# Given an array nums, return the sum of all XOR totals for every subset of nums.
# Note: Subsets with the same elements should be counted multiple times.
# An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
def xor_of_array(nums):
    xor_total = 0
    for i in nums:
        xor_total ^= i
    return xor_total


def sum_xor_of_array(nums):
    result = [[]]
    for i in range(len(nums)):
        n = len(result)
        for j in range(n):
            result.append(result[j] + [nums[i]])
    xor_total = 0

    for i in result:
        # print(i, xor_of_array(i))
        xor_total += xor_of_array(i)
    return xor_total

def subsetXORSum(nums):
    # 'bits' will store the bitwise OR of all numbers
    bits = 0
    for n in nums:
        # Accumulate set bits across all numbers
        print(bits, n)
        bits = bits | n
        # Return the total sum by multiplying 'bits' by 2 raised to the power of (length of 'nums' - 1)
    print(f"bits after for: {bits}, 2 power {len(nums)-1} is {2**(len(nums)-1)}")
    return bits * 2**(len(nums)-1)
# Test cases
# print(sum_xor_of_array([1,3])) # 6
# print(sum_xor_of_array([5,1,6])) # 28
# print(sum_xor_of_array([3,4,5,6,7,8])) # 480
print(subsetXORSum([1,3])) # 6
# print(subsetXORSum([5,1,6])) # 28
# print(subsetXORSum([3,4,5,6,7,8])) # 480
