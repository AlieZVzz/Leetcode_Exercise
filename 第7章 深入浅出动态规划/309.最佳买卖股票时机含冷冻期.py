#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] 最佳买卖股票时机含冷冻期
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, sell_pre = -float("inf"), 0, 0

        for p in prices:
            buy = max(buy, sell_pre - p)
            sell_pre, sell = sell, max(sell, buy + p)
        
        return sell

# @lc code=end

