from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return False


solution = Solution()

arr = [1, 2, 2, 1, 1, 3]
result = solution.uniqueOccurrences(arr=arr)
print(result)
print(result == True)

arr = [1, 2]
result = solution.uniqueOccurrences(arr=arr)
print(result)
print(result == False)

arr = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
result = solution.uniqueOccurrences(arr=arr)
print(result)
print(result == True)
