#
# @lc app=leetcode.cn id=633 lang=python3
#
# [633] 平方数之和
#

# @lc code=start
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.sqrt(c))
        while(left <= right):
            if left*left + right*right == c:
                return True
            elif left*left + right*right < c:
                left += 1
            else:
                right -= 1
        return False
# @lc code=end
