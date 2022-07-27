#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#

# @lc code=start
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        len_t, len_s = len(t), len(s)
        if len_t > len_s: return ''

        char_map = defaultdict(int) # 使用字典储存t中字符
        for char in t:
            char_map[char] += 1
        num_nothave = len(char_map)

        left, right, ans = 0, 0, ''
        while right < len_s:
            while num_nothave and right < len_s: # 向右移动右侧指针
                if s[right] in char_map:
                    char_map[s[right]] -= 1
                    if char_map[s[right]] == 0:
                        num_nothave -= 1
                right += 1
            if right == len_s and num_nothave: break # 如果右侧指针到了结尾，且此刻不构成答案

            while not num_nothave and left < right: # 向左收拢左侧指针
                if s[left] in char_map:
                    char_map[s[left]] += 1
                    if char_map[s[left]] == 1:
                        num_nothave += 1
                left += 1

            if not ans or len(ans) > right - left: # 更新答案
                ans = s[left-1:right]
        return ans

# @lc code=end
