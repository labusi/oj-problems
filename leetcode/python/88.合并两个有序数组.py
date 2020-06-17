#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

from typing import List

# @lc code=start


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = [nums1[i] for i in range(m)]
        i, j = 0, 0
        for k in range(m+n):
            if i >= m:
                nums1[k] = nums2[j]
                j += 1
            elif j >= n:
                nums1[k] = nums1_copy[i]
                i += 1
            else:
                if nums1_copy[i] <= nums2[j]:
                    nums1[k] = nums1_copy[i]
                    i += 1
                else:
                    nums1[k] = nums2[j]
                    j += 1

# @lc code=end
