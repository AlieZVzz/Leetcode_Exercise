#
# @lc app=leetcode.cn id=763 lang=python3
#
# [763] 划分字母区间
#

# @lc code=start
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        intervals = []
        for i in range(0, 26):
            if s.count(chr(ord('a')+i)):
                intervals.append(
                    [s.find(chr(ord("a")+i)), s.rfind(chr(ord("a")+i))])
        intervals = sorted(intervals, key = lambda x: x[0])
        left = intervals[0][0]
        right = intervals[0][1]
        res = []
        for interval in intervals:
            if interval[0] <= right:
                right = max(right, interval[1])
            else:
                res.append([left, right])
                left = interval[0]
                right = interval[1]
        res.append([left, right])
        print(res)
        return [j-i+1 for i, j in res]


# @lc code=end
