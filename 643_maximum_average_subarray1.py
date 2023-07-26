from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_sum = -float('inf')
        for i in range(0, len(nums) - k + 1):
            max_sum = max(max_sum, sum(nums[i:i+k]))
        return max_sum / k


solution = Solution()

nums = [1, 12, -5, -6, 50, 3]
k = 4
result = solution.findMaxAverage(nums=nums, k=k)
print(result)
print(result == 12.75000)

nums = [5]
k = 1
result = solution.findMaxAverage(nums=nums, k=k)
print(result == 5.00000)
