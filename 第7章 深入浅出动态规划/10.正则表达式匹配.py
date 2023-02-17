#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
import re
# @lc code=start
class Solution:
    def isMatch(self, s: str, pattern: str) -> bool:
        if not pattern: return not s
        f_match = bool(s) and pattern[0] in {s[0], '.'}
        if len(pattern) > 1 and pattern[1] == '*':
            return (self.isMatch(s, pattern[2:]) or
                    (f_match and self.isMatch(s[1:], pattern)))
        else:
            return f_match and self.isMatch(s[1:], pattern[1:])
# @lc code=end

