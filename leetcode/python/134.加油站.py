#
# @lc app=leetcode.cn id=134 lang=python3
#
# [134] 加油站
#
from typing import List

# @lc code=start


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        ans = self.helper1(gas, cost)
        return ans

    def helper1(self, gas, cost):
        """
        遍历一次, 记录当前邮箱的剩余油量, 如果剩余小于0了, 则将下一个点作为新的起点.
        中间的节点不可能是起点.
        """
        total, cur = 0, 0
        start = 0
        for i in range(0, len(gas)):
            total += gas[i] - cost[i]
            cur += gas[i] - cost[i]
            if cur < 0:
                start = i+1
                cur = 0
        return start if total >= 0 else -1


if __name__ == "__main__":
    gas = [2, 3, 4]
    cost = [3, 3, 3]
    ans = Solution().canCompleteCircuit(gas, cost)
    print(ans)
# @lc code=end
