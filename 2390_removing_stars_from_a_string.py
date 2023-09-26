from typing import List


class Solution:
    def removeStars(self, s: str) -> str:


solution = Solution()

s = "leet**cod*e"
result = solution.removeStars(s=s)
print(result)
print(result == "lecoe")


s = "erase*****"
result = solution.removeStars(s=s)
print(result)
print(result == "")
