#
# @lc app=leetcode.cn id=416 lang=python3
#
# [416] 分割等和子集
#

# @lc code=start
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sums = sum(nums)
        if sums % 2:
            return False
        target = int(sums/2)
        dp = [False for i in range(target+1)]
        dp[0] = True
        for i in range(1, len(nums)+1):
            for j in range(target, nums[i-1]-1, -1):
                dp[j] = dp[j] or dp[j-nums[i-1]]
        return dp[target]

# @lc code=end
