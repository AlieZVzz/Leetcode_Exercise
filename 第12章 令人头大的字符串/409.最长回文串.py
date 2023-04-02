#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] 最长回文串
#

# @lc code=start
import collections


class Solution:
    def longestPalindrome(self, s: str) -> int:
        ans = 0
        count = collections.Counter(s)
        print(count)
        flag = False    
        for v in count.values():
            ans += v // 2 * 2
            if  v % 2 == 1 and not flag:
                ans += 1
                flag = True
        return ans


# @lc code=end
