from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left = 0
        zero_point = 0
        right = 1
        zero_count = 0
        if nums[0] == 0:
            zero_count += 1
        max_count = 0
        while right < len(nums):
            if nums[right] == 0:
                zero_count += 1
                if zero_count == 2:
                    max_count = max(max_count, right - left - 1)
                    left = zero_point + 1
                    zero_point = right
                    zero_count -= 1
                else:
                    zero_point = right
            max_count = max(max_count, right - left - 1)
            right += 1
        return max(max_count, right - left - 1)


solution = Solution()

nums = [1, 1, 0, 1]
result = solution.longestSubarray(nums=nums)
print(result)
print(result == 3)


nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
result = solution.longestSubarray(nums=nums)
print(result)
print(result == 5)

nums = [1, 1, 1]
result = solution.longestSubarray(nums=nums)
print(result)
print(result == 2)


nums = [1, 1, 0, 0, 1, 1, 1, 0, 1]
result = solution.longestSubarray(nums=nums)
print(result)
print(result == 4)

nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
result = solution.longestSubarray(nums=nums)
print(result)
print(result == 5)
