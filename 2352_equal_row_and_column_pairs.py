from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:


solution = Solution()

grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
result = solution.equalPairs(grid=grid)
print(result)
print(result == 1)


grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
result = solution.equalPairs(grid=grid)
print(result)
print(result == 3)
