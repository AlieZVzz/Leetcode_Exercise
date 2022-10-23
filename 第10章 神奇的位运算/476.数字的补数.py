#
# @lc app=leetcode.cn id=476 lang=python3
#
# [476] 数字的补数
#

# @lc code=start
class Solution:
    def findComplement(self, num: int) -> int:
        for i in range(1,32):
            if 2**i > num:
                return 2**i-num-1
# @lc code=end

