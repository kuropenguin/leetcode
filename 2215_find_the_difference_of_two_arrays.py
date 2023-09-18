from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        num1_set = set(nums1)
        num2_set = set(nums2)
        for num in nums1:
            if num in num2_set:
                num1_set.remove(num)
                num2_set.remove(num)
        return [list(num1_set), list(num2_set)]


solution = Solution()

nums1 = [1, 2, 3]
nums2 = [2, 4, 6]
result = solution.findDifference(nums1=nums1, nums2=nums2)
print(result)
print(result == [[1, 3], [4, 6]])

nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]
result = solution.findDifference(nums1=nums1, nums2=nums2)
print(result)
print(result == [[3], []])
