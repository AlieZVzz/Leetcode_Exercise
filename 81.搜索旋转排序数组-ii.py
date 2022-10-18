#
# @lc app=leetcode.cn id=81 lang=python3
#
# [81] 搜索旋转排序数组 II
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        start = 0
        end = len(nums)-1
        while(start <= end):
            mid = int((start+end)/2)
            if nums[mid] == target:
                return True
            if nums[start] == nums[mid]:
                start += 1
            elif nums[mid] <= nums[end]:
                if (target > nums[mid] and target <= nums[end]):
                    start = mid+1
                else:
                    end = mid-1
            else:
                if (target >= nums[start] and target < nums[mid]):
                    end = mid-1
                else:
                    start = mid+1
        return False

# @lc code=end
