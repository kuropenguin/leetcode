from typing import List


class Solution:
    def decodeString(self, s: str) -> str:


solution = Solution()

s = "3[a]2[bc]"
result = solution.decodeString(s=s)
print(result)
print(result == "aaabcbc")

s = "3[a2[c]]"
result = solution.decodeString(s=s)
print(result)
print(result == "accaccacc")

s = "2[abc]3[cd]ef"
result = solution.decodeString(s=s)
print(result)
print(result == "abcabccdcdcdef")
