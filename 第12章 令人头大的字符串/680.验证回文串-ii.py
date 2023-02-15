#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文串 II
#
# https://leetcode.cn/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (40.09%)
# Likes:    533
# Dislikes: 0
# Total Accepted:    118.9K
# Total Submissions: 296.6K
# Testcase Example:  '"aba"'
#
# 给你一个字符串 s，最多 可以从中删除一个字符。
# 
# 请你判断 s 是否能成为回文字符串：如果能，返回 true ；否则，返回 false 。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：s = "aba"
# 输出：true
# 
# 
# 示例 2：
# 
# 
# 输入：s = "abca"
# 输出：true
# 解释：你可以删除字符 'c' 。
# 
# 
# 示例 3：
# 
# 
# 输入：s = "abc"
# 输出：false
# 
# 
# 
# 提示：
# 
# 
# 1 <= s.length <= 10^5
# s 由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        isPalindrome = lambda s: s == s[::-1]
        strPart = lambda s, x: s[:x] + s[x + 1:]
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return isPalindrome(strPart(s, left)) or isPalindrome(strPart(s, right))
            left += 1
            right -= 1
        return True


# @lc code=end

