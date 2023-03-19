#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
from random import randint
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
    # write code here
        l, r = 0, len(nums)-1
        if k > len(nums) or k < 1: return [] # for passing the damn testcase
        while True:
            pos = self.partition(nums, l, r)
            if pos > k-1:
                l = pos + 1
            elif pos < k-1:
                r = pos - 1
            else:
                return sorted(nums[:pos+1])  # sorted for passing the damn testcase
        
    def partition(self, nums, l, r):
        from random import randint
        p = randint(l, r)
        nums[r], nums[p] = nums[p], nums[r]
        for i, v in enumerate(nums[l:r+1], l):
            if nums[i] <= nums[r]:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
        return l-1  # the pivot index

# @lc code=end

