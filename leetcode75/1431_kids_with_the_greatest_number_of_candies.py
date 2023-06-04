from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = [False] * len(candies)
        max_of_candies = max(candies)
        comparison = max_of_candies - extraCandies
        for i in range(len(candies)):
            if candies[i] >= comparison:
                result[i] = True
        return result


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
