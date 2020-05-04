#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.helper2(prices)

    def helper1(self, prices):
        """
        暴力求解, 枚举全部的买卖可能. 
        Time Limit Exceeded.
        """
        if not prices:
            return 0
        ans = 0
        for i in range(1, len(prices)):
            for j in range(0, i):
                tmp_ans = prices[i] - prices[j]
                if tmp_ans > ans:
                    ans = tmp_ans
        return ans

    def helper2(self, prices):
        """
        动态规划. f[i]: 从[0, i]最合适的买入点, 即目前为止的最小值, 
        每次新读取一条数据, 重新计算最大收益.
        """
        if not prices:
            return 0
        ans, buy_point = 0, 0

        for i in range(1, len(prices)):
            if prices[i] > prices[buy_point]:
                if ans < prices[i] - prices[buy_point]:
                    ans = prices[i] - prices[buy_point]
            else:
                buy_point = i
        return ans


# @lc code=end
