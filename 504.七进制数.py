#
# @lc app=leetcode.cn id=504 lang=python3
#
# [504] 七进制数
#

# @lc code=start
class Solution:
    def convertToBase7(self, num: int) -> str:
        a = ''
        flag = False
        if num == 0:return '0'
        if num < 0:
            flag = True
        num = abs(num)
        while num > 0:
            a += str(num % 7)
            num //= 7
        if flag:
            return '-' + a[::-1]
        return a[::-1]

# @lc code=end

