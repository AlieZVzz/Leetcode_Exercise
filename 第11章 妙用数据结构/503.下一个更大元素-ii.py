#
# @lc app=leetcode.cn id=503 lang=python3
#
# [503] 下一个更大元素 II
#

# @lc code=start
from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        nums_length = len(nums)
        res_list = [-1 for _ in range(nums_length)]
        stack = list()
        
        double_nums = nums + nums
        for index, num in enumerate(double_nums):
            while stack and nums[stack[-1]] < num:
                res_list[stack[-1]] = num
                stack.pop()
            if index < nums_length:
                stack.append(index)
        return res_list
# @lc code=end

