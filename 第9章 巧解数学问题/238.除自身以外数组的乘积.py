#
# @lc app=leetcode.cn id=238 lang=python3
#
# [238] 除自身以外数组的乘积
#

# @lc code=start
from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ans[0] = 1
        # 记录前缀乘积
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        # r是后缀初始值
        r = 1
        for i in range(n - 1, -1, -1):
            ans[i] = ans[i] * r
            # r是后缀乘积
            r = r * nums[i]
        return ans

# @lc code=end

