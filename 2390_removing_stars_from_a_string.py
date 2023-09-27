from typing import List


class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "*" and len(stack) > 0:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)


solution = Solution()

s = "leet**cod*e"
result = solution.removeStars(s=s)
print(result)
print(result == "lecoe")


s = "erase*****"
result = solution.removeStars(s=s)
print(result)
print(result == "")
