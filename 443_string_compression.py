from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        return 1


solution = Solution()

chars = ["a", "a", "b", "b", "c", "c", "c"]
excepted = 6
result = solution.compress(chars=chars)
print(result)
print(result == excepted)

chars = ["a"]
excepted = 1
result = solution.compress(chars=chars)
print(result)
print(result == excepted)

chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
excepted = 4
result = solution.compress(chars=chars)
print(result)
print(result == excepted)
