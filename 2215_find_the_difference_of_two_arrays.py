from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
      return []


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
