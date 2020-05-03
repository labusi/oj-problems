#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接雨水
#

from typing import List
# @lc code=start
class Solution:

    """
    暴力求解;
    动态规划;
    栈;
    双指针;
    """
    def trap(self, height: List[int]) -> int:
        return self.helper3(height)


    def helper1(self, height):
        """
        暴力求解.
        """
        n = len(height)
        ans = 0
        for i in range(1, n-1):
            left_max = height[i]
            for j in range(i-1, -1, -1):
                if height[j] > left_max:
                    left_max = height[j]
            right_max = height[i]
            for j in range(i+1, n):
                if height[j] > right_max:
                    right_max = height[j]
            ans += min(left_max, right_max) - height[i]
        return ans

    def helper2(self, height):
        """
        动态规划.
        """
        n, ans = len(height), 0
        left_max, right_max = [0] * n, [0] * n
        left_max[0], right_max[-1] = height[0], height[-1]
        for i in range(1, n):
            left_max[i] = height[i] if height[i]>=left_max[i-1] else left_max[i-1]
        for j in range(-2, -n-1, -1):
            right_max[j] = height[j] if height[j]>=right_max[j+1] else right_max[j+1]
        for k in range(1, n-1):
            ans += min(left_max[k], right_max[k]) - height[k]

        return ans

    def helper3(self, height):
        """
        双指针.
        Python基础: None, 空字符串, 空列表, 空字典, 空元组, 都相当于False.
        """
        if not height or len(height) < 3:
            return 0
        ans = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]

        while left < right:
            if left_max <= right_max:
                ans += max(0, left_max-height[left])
                left += 1
                left_max = max(left_max, height[left])
            else:
                ans += max(0, right_max-height[right])
                right -= 1
                right_max = max(right_max, height[right])

        return ans


# @lc code=end

