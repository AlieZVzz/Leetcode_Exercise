#
# @lc app=leetcode.cn id=696 lang=python3
#
# [696] 计数二进制子串
#

# @lc code=start
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        seq = [0, 1]
        res = []
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                seq[1] += 1
            else:
                res.append(min(seq))
                seq[0] = seq[1]
                seq[1] = 1
        res.append(min(seq))
        return sum(res)

# @lc code=end

