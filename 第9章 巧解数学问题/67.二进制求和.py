#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        i, j, carry = len(a) - 1, len(b) - 1, 0
        while i >= 0 or j >= 0:
            n1 = int(a[i]) if i >= 0 else 0
            n2 = int(b[j]) if j >= 0 else 0
            tmp = n1 + n2 + carry
            carry = tmp // 2
            res = str(tmp % 2) + res
            i, j = i - 1, j - 1
        return "1" + res if carry else res
# @lc code=end

