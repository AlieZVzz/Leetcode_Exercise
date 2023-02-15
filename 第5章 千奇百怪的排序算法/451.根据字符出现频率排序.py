#
# @lc app=leetcode.cn id=451 lang=python3
#
# [451] 根据字符出现频率排序
#

# @lc code=start
class Solution:
    def frequencySort(self, s: str) -> str:
        dict = {}
        for i in range(0, len(s)):
            if s[i] in dict:
                dict[s[i]] +=1
            else:
                dict[s[i]] = 1
        s = sorted(dict.items(),key=lambda x:x[1], reverse=True)
        return ''.join([i*j for i,j in s])
# @lc code=end

