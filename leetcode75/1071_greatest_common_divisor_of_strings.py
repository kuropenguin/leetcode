class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        longer = ""
        shorter = ""
        if str1 >= str2:
            longer = str1
            shorter = str2
        else:
            longer = str2
            shorter = str1
        for i in range(0, len(shorter), 1):
            checkStr = shorter[:len(shorter) - i]
            if len(shorter) % len(checkStr) != 0 or len(longer) % len(checkStr) != 0:
                continue
            multiOfShorter = len(shorter) // len(checkStr)
            multiOfLonger = len(longer) // len(checkStr)
            if checkStr * multiOfShorter == shorter and checkStr * multiOfLonger == longer:
                return checkStr
        return ""


solution = Solution()

str1 = "ABCABC"
str2 = "ABC"
result = solution.gcdOfStrings(str1=str1, str2=str2)
print(result)
print(result == "ABC")

str1 = "ABABAB"
str2 = "ABAB"
result = solution.gcdOfStrings(str1=str1, str2=str2)
print(result)
print(result == "AB")
