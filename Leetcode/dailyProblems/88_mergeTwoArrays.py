# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

class Solution:
    def merge(self, nums1, nums2, m, n):
        """
        Merges two arrays in non-decreasing order.

        Args:
        nums1 (List[int]): The first array.
        nums2 (List[int]): The second array.
        m (int): The number of elements in nums1.
        n (int): The number of elements in nums2.
        """
        # if(n == 0): return nums1
        if(m == 0 and n > 0): return nums2;
        nums1 = nums1[0:m]
        start_at = 0
        while(start_at < m + n and len(nums2) > 0):
            if(nums1[start_at] > nums2[0]):
                nums1.insert(start_at, nums2.pop(0))
            elif(start_at == len(nums1) - 1):
                nums1.append(nums2.pop(0))
            start_at += 1
            print(f"start_at: {start_at}, nums1: {nums1}, nums2: {nums2}")
        return nums1

# Test cases
solution = Solution()
# print(solution.merge([1, 2, 3, 0, 0, 0], [2, 5, 6], 3, 3))  # [1,2,2,3,5,6]
# print(solution.merge([1], [], 1, 0)) # [1]
print(solution.merge([0], [1], 0, 1)) # [1]
