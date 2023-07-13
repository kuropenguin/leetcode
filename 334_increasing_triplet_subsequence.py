from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        num_1 = float('inf')
        num_2 = float('inf')
        for idx in range(0, len(nums)):
            if num_1 >= nums[idx]:
                num_1 = nums[idx]
            elif num_2 >= nums[idx]:
                num_2 = nums[idx]
            else:
                return True
        return False


solution = Solution()

nums = [1, 2, 3, 4, 5]
excepted = True
result = solution.increasingTriplet(nums=nums)
print(result)
print(result == excepted)


nums = [5, 4, 3, 2, 1]
excepted = False
result = solution.increasingTriplet(nums=nums)
print(result)
print(result == excepted)


nums = [2, 1, 5, 0, 4, 6]
excepted = True
result = solution.increasingTriplet(nums=nums)
print(result)
print(result == excepted)

nums = [20, 100, 10, 12, 5, 13]
excepted = True
result = solution.increasingTriplet(nums=nums)
print(result)
print(result == excepted)
