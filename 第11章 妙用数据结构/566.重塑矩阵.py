#
# @lc app=leetcode.cn id=566 lang=python3
#
# [566] 重塑矩阵
#

# @lc code=start
from typing import List
import itertools
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        nums = list(itertools.chain(*mat))
        ans = []
        for i in range(0, r):
            temp = []
            for j in range(0, c):
                temp.append(nums[i*c+j])
            ans.append(temp)
        return ans

                

# @lc code=end

