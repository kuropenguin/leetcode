from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1
        while left < right:
            h = min(height[left], height[right])
            w = right - left
            maxArea = max(maxArea, h * w)
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
        return maxArea


solution = Solution()

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
excepted = 49
result = solution.maxArea(height=height)
print(result == excepted)


height = [1, 1]
excepted = 1
result = solution.maxArea(height=height)
print(result == excepted)
