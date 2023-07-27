class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        return 1


solution = Solution()

s = "abciiidef"
k = 3
result = solution.maxVowels(s=s, k=k)
print(result)
print(result == 3)


s = "aeiou"
k = 2
result = solution.maxVowels(s=s, k=k)
print(result)
print(result == 2)

s = "leetcode"
k = 3
result = solution.maxVowels(s=s, k=k)
print(result)
print(result == 3)
