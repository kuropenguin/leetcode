from collections import deque


class Solution:
    def longestOnes(self, nums, k):

        left = 0
        res = 0
        # We will store the index of 0 in this deque
        deq = deque()

        for right, num in enumerate(nums):
            if num == 0:
                deq.append(right)
            # When the deque hits the maximum we popleft to remove first zero we countered
            # Similarly we update the left window
            while len(deq) > k:
                idx = deq.popleft()
                left = idx + 1

            res = max(res, right - left + 1)

        return res
