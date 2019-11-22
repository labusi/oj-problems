#
# @lc app=leetcode.cn id=1 lang=python
#
# [1] 两数之和
#

# @lc code=start


class Solution(object):
    def twoSum0(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):  # 不能使用重复的元素
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum(self, nums, target):
        """
        排序之后使用双指针.
        """
        index2val = dict([(index, val) for index, val in enumerate(nums)])
        # 升序排序
        index2val = sorted(index2val.items(), key=lambda item: item[1])
        p1 = 0
        p2 = len(index2val) - 1
        while p1 < p2:
            val1 = index2val[p1][1]
            val2 = index2val[p2][1]
            if val1 + val2 == target:
                return [index2val[p1][0], index2val[p2][0]]
            elif val1 + val2 < target:
                p1 += 1
            else:
                p2 -= 1
        return []

# @lc code=end
