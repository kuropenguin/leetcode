from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """


solution = Solution()

nums = [0, 1, 0, 3, 12]
excepted = [1, 3, 12, 0, 0]
solution.moveZeroes(nums=nums)
print(nums == excepted)
