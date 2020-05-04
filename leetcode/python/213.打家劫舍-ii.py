#
# @lc app=leetcode.cn id=213 lang=python3
#
# [213] 打家劫舍 II
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        198的变体. 主要区别, 房子是一圈的.
        思路, [0, n-2], [1, n-1]两个区间分别处理, 最后去二者的最大.
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        a = self.helper(nums[:-1])
        b = self.helper(nums[1:])
        return max(a, b)

    def helper(self, nums):
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        a, b = nums[0], max(nums[1], nums[0])
        for i in range(2, len(nums)):
            c = max(b, a + nums[i])
            a = b
            b = c

        return b


# @lc code=end
