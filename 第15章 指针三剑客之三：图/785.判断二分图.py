#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] 判断二分图
#

# @lc code=start

from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)

        def dfs(k, c):
            nonlocal ans
            if not ans:
                return
            color[k] = c
            for x in graph[k]:
                if color[x] != -1:
                    if color[x] == c:
                        ans = False
                        return
                else:
                    dfs(x, 1-c)
            return

        color = [-1]*n
        ans = True
        for i in range(n):
            if color[i] == -1:
                dfs(i, 0)
        return ans

# @lc code=end
