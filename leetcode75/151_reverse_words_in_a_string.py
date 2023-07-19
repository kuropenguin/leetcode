class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = []
        for idx in range(len(s)):
            str_list.append(s[idx])
        print(str_list)
        result = ""
        word = ""
        for idx in range(len(str_list)):
            char = str_list.pop()
            if char == " ":
                word = word[::-1]
                if word != "":
                    result += " " + word if result != "" else word
                word = ""
            else:
                word += char
        if result == "":
            result += word[::-1]
        else:
            if word != "":
                result += " " + word[::-1]
        return result


solution = Solution()

s = "the sky is blue"
expected = "blue is sky the"
result = solution.reverseWords(s=s)
print(result)
print(expected)
print(result == expected)

s = "  hello world  "
expected = "world hello"
result = solution.reverseWords(s=s)
print(result)
print(expected)
print(result == expected)
