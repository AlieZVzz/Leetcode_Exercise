#
# @lc app=leetcode.cn id=50 lang=python3
#
# [50] Pow(x, n)
#

# @lc code=start
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow_with_unsigned(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
            ans = pow_with_unsigned(x, n>>1)
            ans *= ans
            if n & 1 == 1:
                ans *= x
            return ans

        if n < 0:
            return 1 / pow_with_unsigned(x, -n)
        else:
            return pow_with_unsigned(x, n)
# @lc code=end

