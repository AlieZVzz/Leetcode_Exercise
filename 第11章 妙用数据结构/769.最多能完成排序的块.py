#
# @lc app=leetcode.cn id=769 lang=python3
#
# [769] 最多能完成排序的块
#

# @lc code=start
from typing import List
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        ans = mx = 0
        for i, x in enumerate(arr):
            mx = max(mx, x)
            ans += mx == i
        return ans

# @lc code=end

