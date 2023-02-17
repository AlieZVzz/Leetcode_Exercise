#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] 单词搜索
#
from typing import List
from collections import Counter
# @lc code=start
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(row, col, idx):
            if idx == w:
                return True
            visited[row][col] = True
            for r, c in [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]:
                if m > r >= 0 and n > c >= 0 and not visited[r][c] and board[r][c] == word[idx]:
                    if backtrack(r, c, idx + 1): return True
            visited[row][col] = False


        m, n = len(board), len(board[0])
        w = len(word)
        # prune
        # bc = Counter(board[r][c] for r in range(m) for c in range(n))
        visited = [[False for _ in range(n)] for _ in range(m)]
        wc = Counter(word)
        # for key in wc.keys():
        #     if wc[key] > bc[key]:
        #         return False
    
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0] and backtrack(row, col, 1):
                    return True
        return False

# @lc code=end
