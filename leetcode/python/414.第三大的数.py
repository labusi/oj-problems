#
# @lc app=leetcode.cn id=414 lang=python3
#
# [414] 第三大的数
#
from typing import List
# @lc code=start


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """
        强行遍历3次.
        """
        a1 = nums[1]
        for num in nums:
            if num >= a1:
                a1 = num
        a2 = -1e64
        for num in nums:
            if num >= a2 and num < a1:
                a2 = num
        if a2 == -1e64:
            return a1
        a3 = -1e64
        for num in nums:
            if num >= a3 and num < a2:
                a3 = num
        if a3 == -1e64:
            return a1
        else:
            return a3


if __name__ == '__main__':
    nums = [2, 2, 3, 1]
    ans = Solution().thirdMax(nums)
    print(ans)
# @lc code=end
