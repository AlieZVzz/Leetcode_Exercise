#
# @lc app=leetcode.cn id=34 lang=python3
#
# [34] 在排序数组中查找元素的第一个和最后一个位置
#

# @lc code=start
from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1] 
        result[0] = self.findStartingIndex(nums, target)  
        result[1] = self.findEndingIndex(nums, target)  
        return result 

    def findStartingIndex(self, nums, target):
        index = -1 
        low, high = 0, len(nums) -1 
        
        while low <= high: 
            mid = low + (high - low)//2 
            
            if nums[mid] == target: 
                index = mid 
                high = mid - 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1      
        return index
        
    def findEndingIndex(self, nums, target):
        index = -1
        low, high = 0, len(nums) -1
        
        while low <= high:
            mid = low + (high - low)//2
            
            if nums[mid] == target:
                index = mid
                low = mid + 1 
            elif nums[mid] > target: 
                high = mid - 1
            else:
                low = mid + 1
        return index


# @lc code=end
