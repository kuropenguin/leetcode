class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        s_idx = 0
        for t_idx in range(0, len(t)):
            if s[s_idx] == t[t_idx]:
                s_idx += 1
                if s_idx == len(s):
                    return True
        return False


solution = Solution()

s = "abc"
t = "ahbgdc"
expected = True
result = solution.isSubsequence(s=s, t=t)
print(result == expected)

s = "axc"
t = "ahbgdc"
expected = False
result = solution.isSubsequence(s=s, t=t)
print(result == expected)
