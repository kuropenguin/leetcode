from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        nums.sort()
        left = 0
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] > k:
                right -= 1
            elif nums[left] + nums[right] < k:
                left += 1
            else:
                count += 1
                left += 1
                right -= 1
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
