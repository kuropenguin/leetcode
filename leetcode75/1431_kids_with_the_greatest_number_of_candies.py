from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [False, False]


solution = Solution()

candies = [2, 3, 5, 1, 3]
extraCandies = 3
excepted = [True, True, True, False, True]

result = solution.kidsWithCandies(candies=candies, extraCandies=extraCandies)
print(result)
print(result == excepted)


candies = [12, 1, 12]
extraCandies = 10
excepted = [True, False, True]

result = solution.kidsWithCandies(candies=candies, extraCandies=extraCandies)
print(result)
print(result == excepted)
