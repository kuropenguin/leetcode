from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = []
        for i in range(len(nums)):
            if i == 0:
                left_sum.append(0)
            else:
                left_sum.append(left_sum[i - 1] + nums[i - 1])
        right_sum = [0 for _ in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                right_sum[i] = 0
            else:
                right_sum[i] = right_sum[i + 1] + nums[i + 1]
        for i in range(len(nums)):
            if left_sum[i] == right_sum[i]:
                return i
        return -1


solution = Solution()

nums = [1, 7, 3, 6, 5, 6]
result = solution.pivotIndex(nums=nums)
print(result)
print(result == 3)

nums = [1, 2, 3]
result = solution.pivotIndex(nums=nums)
print(result)
print(result == -1)

nums = [2, 1, -1]
result = solution.pivotIndex(nums=nums)
print(result)
print(result == 0)
