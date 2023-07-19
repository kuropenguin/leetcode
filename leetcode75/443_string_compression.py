from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        tmp = chars[0]
        result = ''
        for idx in range(1, len(chars)):
            if chars[idx] == tmp[0]:
                tmp += chars[idx]
            else:
                result += self.tmp_compress(tmp)
                tmp = chars[idx]
        result += self.tmp_compress(tmp)
        print(result)
        for idx in range(0, len(result)):
            chars[idx] = result[idx]
        return len(result)

    def tmp_compress(self, string: str) -> str:
        if len(string) == 1:
            return string
        return string[0] + str(len(string))


solution = Solution()

chars = ["a", "a", "b", "b", "c", "c", "c"]
excepted = 6
result = solution.compress(chars=chars)
print(result)
print(result == excepted)

chars = ["a"]
excepted = 1
result = solution.compress(chars=chars)
print(result)
print(result == excepted)

chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
excepted = 4
result = solution.compress(chars=chars)
print(result)
print(result == excepted)
