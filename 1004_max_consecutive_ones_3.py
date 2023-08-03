from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maximun = 0
        for i in range(len(nums)):
            current_k = k
            count = 0
            if nums[i] == 0:
                current_k -= 1
                if current_k > 0:
                    count += 1
                    maximun = max(maximun, count)
                else:
                    maximun = max(maximun, count)
                    continue
            else:
                count += 1
            for j in range(i, len(nums)):
                if nums[j] == 0:
                    current_k -= 1
                    if current_k > 0:
                        count += 1
                        maximun = max(maximun, count)
                    else:
                        maximun = max(maximun, count)
                        break
                else:
                    count += 1
                    maximun = max(maximun, count)
        return maximun


solution = Solution()

nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
k = 2
expected = [1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1]
result = solution.longestOnes(nums=nums, k=k)
print(result)
print(result == 6)

nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
k = 3
expected = [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1]
result = solution.longestOnes(nums=nums, k=k)
print(result)
print(result == 10)
