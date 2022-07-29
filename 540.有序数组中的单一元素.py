#
# @lc app=leetcode.cn id=540 lang=python3
#
# [540] 有序数组中的单一元素
#

# @lc code=start
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        p1 = 0
        p2 = len(nums)-1
        while(p1 < p2):
            mid = (p1+p2)//2
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid+1]:
                p1 = mid+2
            else:
                p2 = mid
        return nums[p1]


# @lc code=end
