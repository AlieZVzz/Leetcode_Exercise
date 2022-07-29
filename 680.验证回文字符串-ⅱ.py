#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        # if s[::-1] == s[::]:
        #     return True
        # for i in range(len(s)):
        #     reversed = s[:i]+s[i+1:]
        #     if reversed[::-1]==reversed[::]:
        #         return True
        # return False
        # p1 = 0
        # p2 = len(s)-1
        # flag = 2
        # flag_1 = True
        # while(p1 <= p2):
        """
        :type s: str
        :rtype: bool
        """
        isPalindrome = lambda x : x == x[::-1]
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return isPalindrome(s[left + 1 : right + 1]) or isPalindrome(s[left: right])
        return True


# @lc code=end
