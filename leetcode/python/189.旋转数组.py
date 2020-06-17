#
# @lc app=leetcode.cn id=189 lang=python3
#
# [189] 旋转数组
#

from typing import List
# @lc code=start


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.helper3(nums, k)

    def helper3(self, nums, k):
        # 先整体反转
        N = len(nums)
        if N <= 1:
            return
        k = k % N
        for i in range(0, N//2):
            nums[i], nums[N-i-1] = nums[N-i-1], nums[i]
        # 反转前k个
        for i in range(0, k//2):
            nums[i], nums[k-i-1] = nums[k-i-1], nums[i]
        # 反转k+1到最后一个元素
        for i in range(k, (k+N)//2):
            nums[i], nums[k+N-1-i] = nums[k+N-1-i], nums[i]

    def helper2(self, nums, k):
        N = len(nums)
        if N <= 1:
            return
        k = k % N
        nums2 = nums[-k:]
        nums1 = nums[:-k]
        nums3 = nums2 + nums1
        for i, num in enumerate(nums3):
            nums[i] = num

    def helper1(self, nums, k):
        """
        超时.
        """
        N = len(nums)
        if N <= 1:
            return
        k = k % N

        for _ in range(k):
            buf = nums[0]
            for i in range(N-1, 0, -1):
                if i == N-1:
                    nums[0] = nums[i]
                else:
                    nums[i+1] = nums[i]
            nums[1] = buf

# @lc code=end
