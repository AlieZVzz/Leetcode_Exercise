#
# @lc app=leetcode.cn id=65 lang=python3
#
# [65] 有效数字
#

# @lc code=start
import re
class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = re.compile('^[+-]?((\d+\.?)|(\d*\.\d+))([eE][+-]?\d+)?$')
        return re.match(pattern, s) !=None
# @lc code=end

