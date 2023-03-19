#
# @lc app=leetcode.cn id=188 lang=python3
#
# [188] 买卖股票的最佳时机 IV
#

# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        k = min(k, len(prices) // 2)

        buy = [-float("inf")] * (k+1)
        sell = [0] * (k+1)

        for p in prices:
            for i in range(1, k+1):
                buy[i] = max(buy[i], sell[i-1] - p)
                sell[i] = max(sell[i], buy[i] + p)
                print(buy[i], sell[i])
        return sell[-1]


# @lc code=end

