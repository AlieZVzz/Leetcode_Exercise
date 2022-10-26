#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为 K 的子数组
#

# @lc code=start
from typing import List
import collections
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        n = len(nums)

        preSums = collections.defaultdict(int)
        preSums[0] = 1

        # 求前缀和数组

        presum = 0
        for i in range(n):
            presum += nums[i]
            
            # if preSums[presum - k] != 0:
            count += preSums[presum - k]   # 利用defaultdict的特性，当presum-k不存在时，返回的是0。这样避免了判断

            preSums[presum] += 1  # 给前缀和为presum的个数加1
            
        return count


        
# @lc code=end

