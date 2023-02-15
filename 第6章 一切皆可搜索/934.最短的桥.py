#
# @lc app=leetcode.cn id=934 lang=python3
#
# [934] 最短的桥
#

# @lc code=start
import collections
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def DFS(i, j):
            if i<0 or i>m-1 or j<0 or j>n-1:
                return
            if grid[i][j]!=1:
                return
            if grid[i][j]==1: 
                grid[i][j]=2
                point_list.append((i,j))
            DFS(i+1,j)
            DFS(i-1,j)
            DFS(i,j+1)
            DFS(i,j-1)

            
        def BFS(root_list):
            queue = collections.deque()
            visited = set()
            for node in root_list:
                queue.append((node, 0))
                visited.add(node)
            while queue:
                (ni, nj), nd = queue.popleft()
                if grid[ni][nj]==1:
                    return nd-1
                for i,j in [(ni-1,nj),(ni+1,nj),(ni,nj+1),(ni,nj-1)]:
                    if i>=0 and i<=m-1 and j>=0 and j<=n-1:
                        if (i,j) not in visited:
                            visited.add((i,j))
                            queue.append(((i,j),nd+1))
            return "NO ANSWER"

        flag = 0
        point_list = []
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    DFS(i,j)
                    flag = 1
                    break
            if flag:
                break
        return BFS(point_list)
            

# @lc code=end

