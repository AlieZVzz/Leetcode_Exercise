#
# @lc app=leetcode.cn id=594 lang=python3
#
# [594] 最长和谐子序列
#

# @lc code=start
from typing import List
import collections
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        ans = 0
        d = collections.Counter(nums)
        for num in nums:
            if num + 1 in d:
                ans = max(ans, d[num] + d[num + 1])
        return ans
# @lc code=end

