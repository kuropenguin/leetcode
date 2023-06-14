class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = list(string)
        for idx in range(len(s)):
            if s[idx] != " ":
                str_list.append(s[idx])
        result = ""
        word = ""
        for idx in range(len(str_list)):
            str = str_list.pop()
            if str == " ":
                word = reverse(word)
                if word != "":
                    result += " " + word
                word = ""
            else:
                word += str
        return " ".join(s.split()[::-1])


solution = Solution()

s = "the sky is blue"
excepted = "blue is sky the"
result = solution.reverseWords(s=s)
print(result)
print(result == excepted)

s = "  hello world  "
expected = "world hello"
result = solution.reverseWords(s=s)
print(result)
print(result == excepted)
