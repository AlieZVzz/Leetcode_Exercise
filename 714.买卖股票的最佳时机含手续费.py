#
# @lc app=leetcode.cn id=714 lang=python3
#
# [714] 买卖股票的最佳时机含手续费
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        buy, sell = -float("inf"), 0

        for p in prices:
            buy = max(buy, sell - p - fee)
            sell = max(sell, buy + p)
        
        return sell

# @lc code=end

