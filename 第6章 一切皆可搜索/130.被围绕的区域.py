#
# @lc app=leetcode.cn id=130 lang=python3
#
# [130] 被围绕的区域
#

# @lc code=start
from typing import List
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        save_point = set()

        def dfs(i, j):
            if i < 0 or i > m-1 or j < 0 or j > n-1 or board[i][j] != 'O':
                return
            if board[i][j] == 'O':
                board[i][j] = '#'
                save_point.add((i, j))
            dfs(i-1, j)
            dfs(i+1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(m):
            for j in (0, n-1):
                if board[i][j] == 'O':
                    save_point.add((i, j))
                    dfs(i, j)
        for i in (0, m-1):
            for j in range(n):
                if board[i][j] == 'O':
                    save_point.add((i, j))
                    dfs(i, j)
        for i in range(m):
            for j in range(n):
                if (i, j) not in save_point:
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'


# @lc code=end
