from typing import List


class Solution:
    def decodeString(self, s: str) -> str:
        idx_pair_map = {}
        left_parenthesis = []
        for idx in range(len(s)):
            if s[idx] == "[":
                left_parenthesis.append(idx)
            elif s[idx] == "]":
                left_idx = left_parenthesis.pop()
                idx_pair_map[left_idx] = idx
        result = ""
        num_str = ""
        idx = 0
        while idx < len(s):
            char = s[idx]
            if char.isdigit():
                num_str += char
            elif char == "[":
                right_idx = idx_pair_map[idx]
                left_idx = idx + 1
                sub_str = s[left_idx:right_idx]
                if num_str == "":
                    result += self.decodeString(s=sub_str)
                else:
                    num = int(num_str)
                    result += num * self.decodeString(s=sub_str)
                    num_str = ""
                idx = right_idx + 1
                continue
            elif char == "]":
                result += char
                idx += 1
                continue
            else:
                result += char
            idx += 1
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
