#
# @lc app=leetcode.cn id=125 lang=python3
#
# [125] 验证回文串
#

# @lc code=start



class Solution:
    def isPalindrome(self, s: str) -> bool:
        res="".join(filter(str.isalnum, s)).lower()
        return res==res[::-1]

# @lc code=end

