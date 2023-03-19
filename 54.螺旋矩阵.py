#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
from typing import List
class Solution:
    def spiralOrder(self, matrix):
        if not matrix or not matrix[0]:
            return []

        res = []
        L, T = 0, 0
        R, B = len(matrix[0])-1, len(matrix)-1
        sum = len(matrix[0]) * len(matrix)
        
        while sum >= 1:
            for i in range(L, R+1):
                if sum >= 1:
                    res.append(matrix[T][i])
                    sum -= 1
            T += 1
            for i in range(T, B+1):
                if sum >= 1:
                    res.append(matrix[i][R])
                    sum -= 1
            R -= 1
            for i in range(R, L-1, -1):
                if sum >= 1:
                    res.append(matrix[B][i])
                    sum -= 1
            B -= 1
            for i in range(B, T-1, -1):
                if sum >= 1:
                    res.append(matrix[i][L])
                    sum -= 1
            L += 1
        return res



            
# test = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# testclass = Solution()
# print(testclass.spiralOrder(test))
# @lc code=end

