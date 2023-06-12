class Solution:
    def reverseVowels(self, s: str) -> str:
        return ""


solution = Solution()

s = "hello"
excepted = "holle"
result = solution.reverseVowels(s=s)
print(result)
print(result == excepted)

s = "leetcode"
expect = "leotcede"
result = solution.reverseVowels(s=s)
print(result)
print(result == expect)
