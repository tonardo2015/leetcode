# leetcode 15
from typing import List

class Solution:
    def three_sum(self, nums):
        res = []
        nums.sort()
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                curr = nums[i] + nums[left] + nums[right]
                if curr == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif curr < 0:
                    left += 1
                else:
                    right -= 1
        return res
