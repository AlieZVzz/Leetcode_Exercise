#
# @lc app=leetcode.cn id=342 lang=python3
#
# [342] 4的幂
#

# @lc code=start
import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        return math.log(n, 4)%1==0
# @lc code=end

