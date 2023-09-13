from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        result = 0
        total = 0
        for i in range(0, len(gain)):
            total += gain[i]
            result = max(result, total)
        return result


solution = Solution()

gain = [-5, 1, 5, 0, -7]
result = solution.largestAltitude(gain=gain)
print(result)
print(result == 1)


gain = [-4, -3, -2, -1, 4, 3, 2]
result = solution.largestAltitude(gain=gain)
print(result)
print(result == 0)
