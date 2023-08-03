class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set(['a', 'e', 'i', 'o', 'u'])
        if k > len(s):
            return 0
        max_vowels = 0
        window = []
        # 初期化
        for i in range(k):
            window.append(s[i])
            if s[i] in vowels:
                max_vowels += 1

        current_vowels = max_vowels
        for i in range(k, len(s)):
            first = window.pop(0)
            window.append(s[i])
            if first in vowels:
                current_vowels -= 1
            if s[i] in vowels:
                current_vowels += 1
            max_vowels = max(max_vowels, current_vowels)
            if max_vowels == k:
                return k
            print(first, s[i], current_vowels)
        return max_vowels


solution = Solution()

# s = "abciiidef"
# k = 3
# result = solution.maxVowels(s=s, k=k)
# print(result)
# print(result == 3)


# s = "aeiou"
# k = 2
# result = solution.maxVowels(s=s, k=k)
# print(result)
# print(result == 2)

# s = "leetcode"
# k = 3
# result = solution.maxVowels(s=s, k=k)
# print(result)
# print(result == 2)

s = "weallloveyou"
k = 7
result = solution.maxVowels(s=s, k=k)
print(result)
print(result == 4)
