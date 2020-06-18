#
# @lc app=leetcode.cn id=219 lang=python3
#
# [219] 存在重复元素 II
#
from typing import List

# @lc code=start


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        tb = {}
        for idx, num in enumerate(nums):
            tb[num] = tb.get(num, [])
            tb[num].append(idx)
            tmp = tb[num][-2:]
            if len(tmp) == 2 and tmp[-1] - tmp[-2] <= k:
                return True

        return False


if __name__ == "__main__":
    s = Solution()
    nums = [1, 2, 3, 1]
    k = 3
    ans = s.containsNearbyDuplicate(nums, k)
    print(ans)
# @lc code=end
