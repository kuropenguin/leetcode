from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        return 1


solution = Solution()

nums = [1, 1, 0, 1]
result = solution.longestSubarray(nums=nums)
print(result)
print(result == 3)


nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
result = solution.longestSubarray(nums=nums)
print(result)
print(result == 5)

nums =[1,1,1]
result = solution.longestSubarray(nums=nums)
print(result)
print(result == 2)
