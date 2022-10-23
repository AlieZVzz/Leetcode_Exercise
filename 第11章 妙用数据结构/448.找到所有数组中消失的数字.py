#
# @lc app=leetcode.cn id=448 lang=python3
#
# [448] 找到所有数组中消失的数字
#

# @lc code=start
from typing import List
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        counter = set(nums)
        N = len(nums)
        res = []
        for i in range(1, N + 1):
            if i not in counter:
                res.append(i)
        return res




# @lc code=end

