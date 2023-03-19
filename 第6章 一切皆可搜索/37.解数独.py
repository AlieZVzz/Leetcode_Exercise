#
# @lc app=leetcode.cn id=37 lang=python3
#
# [37] 解数独
#

# @lc code=start
from typing import List
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def backtrack(board, i, j):
            """i, j代表遍历到的行、列索引"""
            if j == 9:                  # 遍历完最后一列后，转去遍历下一行
                return backtrack(board, i+1, 0)
            if i == 9:                  # 遍历完最后一行后，结束
                return True
            if board[i][j] != '.':      # 非空位置不用管
                return backtrack(board, i, j+1)
            for n in range(1, 10):      # 遍历选择列表，此处的选择是，给空白处填 "1" - "9" 中之一
                c = str(n)
                if not self.check(board, i, j, c):     # 判断选择的字符是否满足要求（不与其他位置冲突）
                    continue
                board[i][j] = c                 # 做出选择
                if backtrack(board, i, j+1):    # 递归调用，直接return是因为只需要一个可行解，而不需要所有可行解
                    return True
                board[i][j] = '.'               # 撤销选择
        backtrack(board, 0, 0)

    def check(self, board, row, col, c):
        for i in range(9):
            if board[row][i] == c:
                return False
            if board[i][col] == c:
                return False
            if board[(row//3)*3 + i // 3][(col//3)*3 + i % 3] == c:
                return False
        return True

# @lc code=end

