#
# @lc app=leetcode.cn id=312 lang=python3
#
# [312] 戳气球
#

# @lc code=start
from typing import List
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        if len(set(nums)) == 1 and len(nums) > 1:
            return nums[0]**3*(len(nums)-2)+nums[0]**2+nums[0]
        
        def getMaxCoins(i, j):
            if i == j - 1:
                return 0
            if memo[i][j] > 0:
                return memo[i][j]
            temp = 0
            for k in range(i + 1, j):
                left = getMaxCoins(i, k)
                right = getMaxCoins(k, j)
                temp = max(temp, left + right + nums[i] * nums[k] * nums[j])
            memo[i][j] = temp
            return temp
    
        nums = [1, *nums, 1]
        memo = [[0 for i in nums] for n in nums]
        return getMaxCoins(0, len(nums) - 1)


# @lc code=end

