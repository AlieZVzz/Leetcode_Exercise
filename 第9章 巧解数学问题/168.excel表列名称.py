#
# @lc app=leetcode.cn id=168 lang=python3
#
# [168] Excel表列名称
#

# @lc code=start

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        ans = list()
        while columnNumber > 0:
            a0 = (columnNumber - 1) % 26 + 1
            ans.append(chr(a0 - 1 + ord("A")))
            columnNumber = (columnNumber - a0) // 26
        return "".join(ans[::-1])

        # s = ''
        # while(n):
        #     n -= 1
        #     s = chr(n%26+65) + s
        #     n = n//26
        # return s


        
# @lc code=end

