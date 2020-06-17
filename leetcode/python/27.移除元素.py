#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#
from typing import List

# @lc code=start


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        N = len(nums)
        count = 0 if nums[0] != val else 1

        for i in range(1, N):
            if nums[i] == val:
                count += 1
            else:
                j = i
                while j-1 >= 0 and nums[j-1] == val:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
                    j -= 1

        return N-count
# @lc code=end
