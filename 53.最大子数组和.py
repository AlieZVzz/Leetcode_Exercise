#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子数组和
#

# @lc code=start
from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-1000000]*len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i-1]<0:    
                dp[i] = nums[i]
            else:      
                dp[i] =  max(dp[i], nums[i]+dp[i-1])
        return max(dp)
# @lc code=end

#  class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#          """
#         for i in range(1, len(nums)):
#             nums[i]= nums[i] + max(nums[i-1], 0)
#         return max(nums)