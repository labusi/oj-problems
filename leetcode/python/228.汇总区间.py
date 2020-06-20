#
# @lc app=leetcode.cn id=228 lang=python3
#
# [228] 汇总区间
#

from typing import List

# @lc code=start


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i, j = 0, 0
        res = []
        N = len(nums)
        while j < N:
            if j+1 < N and nums[j] == nums[j+1]-1:
                j += 1
            else:
                if i != j:
                    res.append("%d->%d" % (nums[i], nums[j]))
                else:
                    res.append(str(nums[i]))
                i = j = j+1

        return res


if __name__ == "__main__":
    nums = [0, 1, 2, 4, 5, 7]
    s = Solution()

    ans = s.summaryRanges(nums)
    print(ans)
# @lc code=end
