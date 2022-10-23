#
# @lc app=leetcode.cn id=693 lang=python3
#
# [693] 交替位二进制数
#

# @lc code=start
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        temp=n^(n>>1)
        return (temp&(temp+1))==0
# @lc code=end

