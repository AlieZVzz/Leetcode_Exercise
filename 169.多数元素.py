#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#

# @lc code=start
from typing import Optional, List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            if ans == 0:
                res = i
            if i == res:
                ans +=1 
            else:
                ans -=1
        return res
# @lc code=end

