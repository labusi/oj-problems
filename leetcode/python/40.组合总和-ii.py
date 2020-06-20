#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

from typing import List

# @lc code=start


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        nums = sorted(candidates)
        paths = []
        path = []
        self.helper(nums, 0, paths, path, target)
        return paths

    def helper(self, nums, start, paths, path, target):

        if target < 0:
            return

        if target == 0:
            paths.append(path[:])
            return

        for i, num in enumerate(nums[start:], start):
            if i > start and num == nums[i-1]:
                continue
            path.append(num)
            self.helper(nums, i+1, paths, path, target-num)
            if len(path) > 0:
                path.pop()
            if target - num < 0:
                break


if __name__ == "__main__":
    nums = [10, 1, 2, 7, 6, 1, 5]
    target = 8

    s = Solution()
    paths = s.combinationSum2(nums, target)
    print(paths)

# @lc code=end
