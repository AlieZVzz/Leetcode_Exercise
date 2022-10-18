#
# @lc app=leetcode.cn id=646 lang=python3
#
# [646] 最长数对链
#

# @lc code=start
from typing import List
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        dp = [1] * n
        ans = 1
        pairs.sort(key=lambda a: a[0])
        for i in range(n):
            for j in range(i):
                if pairs[i][0] > pairs[j][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    ans = max(ans, dp[i])
        return ans


# @lc code=end

