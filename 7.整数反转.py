#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        rev_num = int(str(abs(x))[::-1])
        x_rev = rev_num if x >= 0 else (-1)*rev_num
        if -2**31 <= x_rev <= 2**31 - 1:
            return x_rev
        return 0

# @lc code=end

