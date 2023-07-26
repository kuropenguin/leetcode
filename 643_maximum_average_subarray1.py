from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        return 1


solution = Solution()

nums = [1, 12, -5, -6, 50, 3]
k = 4
result = solution.findMaxAverage(nums=nums, k=k)
print(result == 12.75000)

nums = [5]
k = 1
result = solution.findMaxAverage(nums=nums, k=k)
print(result == 5.00000)
