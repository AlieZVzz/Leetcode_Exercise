#
# @lc app=leetcode.cn id=509 lang=python3
#
# [509] 斐波那契数
#

# @lc code=start
class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        p,q,r = 0,0,1
        for i in range(2, n+1):
            p,q = q,r
            r = p+q
        return r
# @lc code=end

