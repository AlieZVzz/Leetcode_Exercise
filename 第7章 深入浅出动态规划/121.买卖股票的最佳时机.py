#
# @lc app=leetcode.cn id=121 lang=python3
#
# [121] 买卖股票的最佳时机
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell = 0
        buy = -10000
        for i in range(len(prices)):
            buy = max(buy, -prices[i])
            sell = max(sell, buy+prices[i])
        return sell
# @lc code=end
