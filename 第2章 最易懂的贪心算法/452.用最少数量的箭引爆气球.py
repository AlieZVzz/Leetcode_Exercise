#
# @lc app=leetcode.cn id=452 lang=python3
#
# [452] 用最少数量的箭引爆气球
#

# @lc code=start
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda balloon: balloon[1])
        arrows = 1
        target = points[0][1]
        for i in range(len(points)):
            if target < points[i][0]:
                target = points[i][1]
                arrows += 1
        return arrows

# @lc code=end
