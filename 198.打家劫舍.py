#
# @lc app=leetcode.cn id=198 lang=python3
#
# [198] 打家劫舍
#

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        p1,p2 = 0,0
        for i in range(n):
            cur = max(p1,p2+nums[i])
            p2 = p1
            p1 = cur
        return cur
# @lc code=end

