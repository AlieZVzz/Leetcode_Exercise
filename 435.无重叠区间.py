#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] 无重叠区间
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                ans += 1
                if intervals[i][1] > intervals[i-1][1]:
                    intervals[i] = intervals[i-1]
        return ans
# @lc code=end

