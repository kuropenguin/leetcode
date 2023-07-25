from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == k:
                    nums.pop(i)
                    nums.pop(j - 1)
                    count += 1
        return count


solution = Solution()

nums = [1, 2, 3, 4]
k = 5
result = solution.maxOperations(nums=nums, k=k)
print(result == 2)


nums = [3, 1, 3, 4, 3]
k = 6
result = solution.maxOperations(nums=nums, k=k)
print(result == 1)
