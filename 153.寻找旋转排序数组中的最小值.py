#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#

# @lc code=start
from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        p , q = 0, len(nums)-1
        
        while(p<q):
            mid = (p+q)//2
            print(mid)
            if nums[mid]>=nums[q]:
                p = mid+1
            else:
                q = mid
        return nums[p]

# @lc code=end

