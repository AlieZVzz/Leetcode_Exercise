#
# @lc app=leetcode.cn id=474 lang=python3
#
# [474] 一和零
#

# @lc code=start
from typing import List
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1) for i in range(m+1)]

        for s in strs:
            zeroNum = s.count("0")
            oneNum = s.count("1")
            for i in range(m, zeroNum-1,-1):
                for j in range(n, oneNum-1, -1):
                    dp[i][j] = max(dp[i-zeroNum][j-oneNum]+1, dp[i][j])
        return dp[-1][-1]
# @lc code=end

