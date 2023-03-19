#
# @lc app=leetcode.cn id=326 lang=python3
#
# [326] 3 的幂
#

# @lc code=start

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        num_set = set(pow(3,i)  for i in range(31))
        return n in num_set


# @lc code=end

