from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for idx in range(len(flowerbed)):
            prev = 0 if idx == 0 else flowerbed[idx - 1]
            next = 0 if idx == len(flowerbed) - 1 else flowerbed[idx + 1]
            if prev == 0 and next == 0 and flowerbed[idx] == 0:
                flowerbed[idx] = 1
                n -= 1
            if n <= 0:
                return True
        return False


solution = Solution()

flowerbed = [1, 0, 0, 0, 1]
n = 1
excepted = True
result = solution.canPlaceFlowers(flowerbed=flowerbed, n=n)
print(result == excepted)


flowerbed = [1, 0, 0, 0, 1]
n = 2
excepted = False
result = solution.canPlaceFlowers(flowerbed=flowerbed, n=n)
print(result == excepted)
