#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#
from typing import List

# @lc code=start


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.helper3(nums)

    def helper1(self, nums):
        notZeroNums = []
        for num in nums:
            if num != 0:
                notZeroNums.append(num)

        for i in range(len(nums)):
            if i < len(notZeroNums):
                nums[i] = notZeroNums[i]
            else:
                nums[i] = 0

    def helper2(self, nums):
        """
        从数组结尾开始扫描, 如果元素是0, 则将其移动到其后面最近的0的前面.
        """
        N = len(nums)
        j = N - 1
        while j >= 0:
            if nums[j] == 0:
                k = j
                while k+1 < N and nums[k+1] != 0:
                    nums[k], nums[k+1] = nums[k+1], nums[k]
                    k += 1
            j -= 1

    def helper3(self, nums):
        """
        提高算法效率的本质, 就是避免一切不必要的计算.
        i, j区间是一个连续0的区间, 这个区间向右移动时, 如果碰到非0的元素就和区间开始的元素交换; 碰到0元素就吞并.
        """
        N = len(nums)
        i = 0
        for j in range(N):
            if nums[j] != 0:
                if i != j:
                    nums[i], nums[j] = nums[j], nums[i]
                i += 1

    def helper4(self, nums):
        """
        这样会把0都移动到左边.
        """
        N = len(nums)
        i = N - 1
        for j in range(N-1, -1, -1):
            if nums[j] != 0:
                if i != j:
                    nums[j], nums[i] = nums[i], nums[j]
                i -= 1


if __name__ == "__main__":
    nums = [0, 1, 0, 12, 34]
    s = Solution()
    s.moveZeroes(nums)
    print(nums)


# @lc code=end
