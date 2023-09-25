from typing import List


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        w1_dict = {}
        for w in word1:
            if w in w1_dict:
                w1_dict[w] += 1
            else:
                w1_dict[w] = 1
        w2_dict = {}
        for w in word2:
            if w in w2_dict:
                w2_dict[w] += 1
            else:
                w2_dict[w] = 1
        for w in word1:
            if w not in w2_dict:
                return False
        w1_values = sorted(w1_dict.values())
        w2_values = sorted(w2_dict.values())
        return w1_values == w2_values


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
