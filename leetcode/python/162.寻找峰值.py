#
# @lc app=leetcode.cn id=162 lang=python3
#
# [162] 寻找峰值
#

# @lc code=start
class Solution:
    """
    二分查找的思路:
    1. 如果mid位置满足条件则直接返回结果
    2. 如果mid处于升序区间, 说明右半部分必定有解, 因为nums[n] = -inf
    3. 如果mid处于降序区间, 说明左半部分必定有解, 因为nums[-1] = -inf
    """

    def findPeakElement(self, nums: List[int]) -> int:
        return self.helper2(nums)

    def helper1(self, nums):
        if not nums:
            return None
        n = len(nums)
        for i in range(n):
            right = nums[i + 1] if i < n - 1 else nums[i] - 1
            if nums[i] > right:
                return i

    def helper2(self, nums):
        if not nums:
            return None
        n = len(nums)
        a, b = 0, n - 1
        while b - a > 1:
            mid = (a + b) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid - 1] < nums[mid] and nums[mid] < nums[mid + 1]:
                a = mid
            else:
                b = mid

        if nums[a] > nums[b]:
            return a
        else:
            return b


# @lc code=end
