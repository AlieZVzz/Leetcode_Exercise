#
# @lc app=leetcode.cn id=51 lang=python3
#
# [51] N 皇后
#

# @lc code=start

from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(row):
            n = len(board)
            if row == n:
                tmp = [''.join(i) for i in board]
                res.append(tmp)
                return

            for col in range(n):
                if not self.IsValid(board, row, col):
                    continue
                board[row][col] = 'Q'
                backtrack(row+1)
                board[row][col] = '.'

        board = [['.'] * n for _ in range(n)]
        res = []
        backtrack(0)
        return res

    def IsValid(self, board, row, col):
        n = len(board)

        for i in range(row):
            if board[i][col] == 'Q':
                return False
        for i, j in zip(range(row-1, -1, -1), range(col+1, n, 1)):
            if board[i][j] == 'Q':
                return False
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        return True
# @lc code=end
