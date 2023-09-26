from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        col_list = []
        for idx in range(0, len(grid)):
            col = []
            for list in grid:
                col.append(list[idx])
            col_list.append(col)

        count = 0
        for row in grid:
            for col in col_list:
                if row == col:
                    count += 1
        return count


solution = Solution()

grid = [[3, 2, 1], [1, 7, 6], [2, 7, 7]]
result = solution.equalPairs(grid=grid)
print(result)
print(result == 1)


grid = [[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]
result = solution.equalPairs(grid=grid)
print(result)
print(result == 3)
