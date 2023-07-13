from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        for idx in range(0, len(nums)):
            if idx == 0:
                pre[idx] = 1
            else:
                pre[idx] = pre[idx - 1] * nums[idx - 1]
        next = [1] * len(nums)
        for idx in range(len(nums) - 1, -1, -1):
            if idx == len(nums) - 1:
                next[idx] = 1
            else:
                next[idx] = next[idx+1] * nums[idx + 1]
        ans = [1] * len(nums)
        for idx in range(0, len(nums)):
            ans[idx] = pre[idx] * next[idx]
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
