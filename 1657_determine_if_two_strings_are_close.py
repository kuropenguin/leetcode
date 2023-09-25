from typing import List


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return True


solution = Solution()

word1 = "abc"
word2 = "bca"
result = solution.closeStrings(word1=word1, word2=word2)
print(result)
print(result == True)


word1 = "a"
word2 = "aa"
result = solution.closeStrings(word1=word1, word2=word2)
print(result)
print(result == False)

word1 = "cabbba"
word2 = "abbccc"
result = solution.closeStrings(word1=word1, word2=word2)
print(result)
print(result == True)
