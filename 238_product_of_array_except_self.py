from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    ans[i] *= nums[j]
        return ans


solution = Solution()

nums = [1, 2, 3, 4]
excepted = [24, 12, 8, 6]
result = solution.productExceptSelf(nums=nums)
print(result)
print(result == excepted)

nums = [-1, 1, 0, -3, 3]
excepted = [0, 0, 9, 0, 0]
result = solution.productExceptSelf(nums=nums)
print(result)
print(result == excepted)
