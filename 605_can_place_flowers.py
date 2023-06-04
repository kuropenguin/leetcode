from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        return False


solution = Solution()

flowerbed = [1, 0, 0, 0, 1]
n = 1
excepted = True
result = solution.kidsWithCandies(flowerbed=flowerbed, n=n)
print(result)


flowerbed = [1, 0, 0, 0, 1]
n = 2
excepted = False
result = solution.kidsWithCandies(flowerbed=flowerbed, n=n)
print(result)
