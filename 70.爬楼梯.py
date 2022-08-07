#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<2:
            return n
        p,q,r = 0,1,1
        for i in range(2, n+1):
            p,q = q,r
            r = p+q
        return r
# @lc code=end

