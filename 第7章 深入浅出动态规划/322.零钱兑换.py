#
# @lc app=leetcode.cn id=322 lang=python3
#
# [322] 零钱兑换
#

# @lc code=start
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1]*(amount + 1)
        dp[0] = 0
        # 遍历物品
        for j in range(1, amount + 1):
            # 遍历背包
            for coin in coins:
                if j >= coin:
                    dp[j] = min(dp[j], dp[j - coin] + 1)
        return dp[amount] if dp[amount] < amount + 1 else -1
# @lc code=end
