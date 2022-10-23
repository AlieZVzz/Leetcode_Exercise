#
# @lc app=leetcode.cn id=455 lang=python3
#
# [455] 分发饼干
#

# @lc code=start
from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        num = 0
        for i in g:
            for j in s:
                if i<=j:
                    num+=1
                    s.remove(j)
                    break
        return num

# @lc code=end

