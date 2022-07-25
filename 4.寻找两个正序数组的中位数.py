#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        data = list(sorted(nums1))
        half = len(data) // 2
        median = (data[half] + data[~half]) / 2
        return median
# @lc code=end
