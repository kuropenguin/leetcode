from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for idx in range(0, len(nums)):
            if nums[idx] == 0:
                for jdx in range(idx + 1, len(nums)):
                    if nums[jdx] != 0:
                        nums[idx], nums[jdx] = nums[jdx], nums[idx]
                        break


solution = Solution()

nums = [0, 1, 0, 3, 12]
excepted = [1, 3, 12, 0, 0]
solution.moveZeroes(nums=nums)
print(nums)
print(excepted)
print(nums == excepted)

nums = [0]
excepted = [0]
solution.moveZeroes(nums=nums)
print(nums)
print(excepted)
print(nums == excepted)
