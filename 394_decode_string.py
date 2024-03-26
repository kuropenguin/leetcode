from typing import List


class Solution:
    def decodeString(self, s: str) -> str:
        # please write code
        # here
        stack = []
        for char in s:
            if char == "]":
                temp = ""
                while stack[-1] != "[":
                    temp = stack.pop() + temp
                stack.pop()
                num = ""
                while len(stack) > 0 and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * temp)
            else:
                stack.append(char)
        return result


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
