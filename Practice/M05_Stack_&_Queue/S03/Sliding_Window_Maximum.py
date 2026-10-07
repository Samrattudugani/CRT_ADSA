# 239
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        deq = deque()
        result = []
        for i, num in enumerate(nums):
            while deq and nums[deq[-1]] <= num:
                deq.pop()
            deq.append(i)
            if deq[0] <= i - k:
                deq.popleft()
            if i >= k - 1:
                result.append(nums[deq[0]])
        return result