#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

from typing import List

# @lc code=start


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.helper3(nums)

    def helper1(self, nums):
        zeroCount = 0
        oneCount = 0
        for num in nums:
            if num == 0:
                zeroCount += 1
            if num == 1:
                oneCount += 1

        for i in range(len(nums)):
            if i < zeroCount:
                nums[i] = 0
            elif i >= zeroCount and i < zeroCount + oneCount:
                nums[i] = 1
            else:
                nums[i] = 2

    def helper2(self, nums):
        """
        does not work.
        """
        N = len(nums)
        i = 0
        for j in range(0, N):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

    def helper3(self, nums):
        """
        分析:
        初始条件下, p0和cur指向同一个位置,
            如果此时元素是0, 那么cur和p0同时向右移动一个单位;
            如果碰到了1, 则cur右移一个单位, p0保持, 因为此时p0的位置就是0的右边界
            如果碰到了2, 则需要将cur和p2位置的元素进行交换, 并将p2左移一个单位, 而cur保持(因为交换回来的元素是什么不知道,需要再下一个循环时进行处理)
        """
        N = len(nums)
        p0, p2 = 0, N-1
        cur = 0

        while cur <= p2:
            if nums[cur] == 0:
                if cur != p0:
                    nums[p0], nums[cur] = nums[cur], nums[p0]
                cur += 1
                p0 += 1
            elif nums[cur] == 2:
                nums[cur], nums[p2] = nums[p2], nums[cur]
                p2 -= 1
            else:
                cur += 1


# @lc code=end
