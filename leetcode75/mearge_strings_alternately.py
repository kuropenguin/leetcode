class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        max_length = max(len(word1), len(word2))
        for i in range(max_length):
            w1 = ""
            if i <= len(word1) - 1:
                w1 = word1[i]
            w2 = ""
            if i <= len(word2) - 1:
                w2 = word2[i]
            result += w1 + w2
        return result


solution = Solution()

print(solution.mergeAlternately(word1="abc", word2="pqr"))
