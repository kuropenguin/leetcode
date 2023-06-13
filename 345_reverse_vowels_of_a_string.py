from collections import deque
class Solution:
    def reverseVowels(self, string: str) -> str:
        idx_stack = []
        str_queue = deque()
        str_list = list(string)
        for idx in range(len(string)):
            if string[idx] in "aeiouAEIOU":
                idx_stack.append(idx)
                str_queue.append(string[idx])
        while idx_stack:
            idx = idx_stack.pop()
            s = str_queue.popleft()
            str_list[idx] = s

        return "".join(str_list)


solution = Solution()

s = "hello"
excepted = "holle"
result = solution.reverseVowels(string=s)
print(result)
print(result == excepted)

s = "leetcode"
expect = "leotcede"
result = solution.reverseVowels(string=s)
print(result)
print(result == expect)
