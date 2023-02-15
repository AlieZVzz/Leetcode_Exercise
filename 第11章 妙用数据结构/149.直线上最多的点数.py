#
# @lc app=leetcode.cn id=149 lang=python3
#
# [149] 直线上最多的点数
#

# @lc code=start
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        explored = set()
        ans = 1
        for i in range(len(points)):
            for j in range(i+1, len(points)):
                curr = 2
                dx, dy = points[j][0] - \
                    points[i][0], points[j][1] - points[i][1]
                for k in range(j+1, len(points)):
                    if (i, j) in explored or (i, k) in explored or (j, k) in explored:
                        continue
                    if dy * (points[k][0] - points[j][0]) == (points[k][1] - points[j][1]) * dx:
                        curr += 1
                        explored.add((j, k))
                        explored.add((i, k))
                ans = max(ans, curr)
        return ans

# @lc code=end
