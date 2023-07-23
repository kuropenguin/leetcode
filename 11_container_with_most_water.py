from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:


solution = Solution()

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
excepted = 49
result = solution.maxArea(height == height)
print(result == excepted)


height = [1, 1]
excepted = 1
result = solution.maxArea(height == height)
print(result == excepted)
