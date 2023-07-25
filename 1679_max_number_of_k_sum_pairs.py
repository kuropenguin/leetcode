from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        return 1


solution = Solution()

nums = [1, 2, 3, 4]
k = 5
result = solution.maxOperations(nums=nums, k=k)
print(result == 2)


nums = [3, 1, 3, 4, 3]
k = 6
result = solution.maxOperations(nums=nums, k=k)
print(result == 1)
