#
# @lc app=leetcode.cn id=695 lang=python3
#
# [695] 岛屿的最大面积
#

# @lc code=start


from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def search_island(grid, x, y):
            if not 0 <= x < len(grid) or not 0 <= y < len(grid[0]) or not grid[x][y]:
                return
            grid[x][y] = 0
            self.result += 1
            search_island(grid, x, y+1)
            search_island(grid, x, y-1)
            search_island(grid, x+1, y)
            search_island(grid, x-1, y)
            return self.result
        maxinum = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == 1:
                    self.result = 0 
                    maxinum = max(maxinum,search_island(grid, i, j))
        return maxinum

# @lc code=end
