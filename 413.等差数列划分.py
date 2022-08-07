#
# @lc app=leetcode.cn id=413 lang=python3
#
# [413] 等差数列划分
#

# @lc code=start

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums)-2):
            for j in range(i+2,len(nums)):
                if (nums[j] - nums[j-1] == nums[j-1] - nums[j-2]):
                    ans+=1
                else:
                    break
        return ans



# @lc code=end
