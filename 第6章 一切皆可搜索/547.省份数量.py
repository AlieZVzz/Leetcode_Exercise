#
# @lc app=leetcode.cn id=547 lang=python3
#
# [547] 省份数量
#

# @lc code=start
from typing import List
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = set()
        n = len(isConnected)
        # 将i所在的省份加入visited

        def dfs(i):
            for j in range(n):
                # 这里加入 j not in visited 的判断特别重要
                # 加上这句话 如果每一个j都出现在里visited中 则不会向下递归 不加则无穷向下递归
                if isConnected[i][j] == 1 and j not in visited:
                    visited.add(j)
                    dfs(j)
        # 遍历所有的城市
        num_prov = 0
        for i in range(n):
            # 如果i不在之前遍历过的省份
            if i not in visited:
                num_prov += 1
            # 将i所在省份的城市纳入visited
                dfs(i)
        return num_prov

# @lc code=end
