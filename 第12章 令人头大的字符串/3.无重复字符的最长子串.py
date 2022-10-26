#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, i = {}, 0, -1  # i是左指针
        for j in range(len(s)):  # j是右指针
            if s[j] in dic:  # 若当前元素在之前出现过，更新左指针
                # 当之前出现的元素在左右指针中间，左指针更新为之前元素下标，若不在中间，左指针不变
                i = max(i, dic[s[j]])
            dic[s[j]] = j  # 将当前元素加入哈希表中
            res = max(res, j - i)
        return res

# @lc code=end
