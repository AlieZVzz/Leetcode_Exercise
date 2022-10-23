#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(tmp, cur, index):
            if cur > target:
                return
            if cur == target:
                res.append(tmp)
                return
            for i in range(index, n):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(tmp + [candidates[i]], cur + candidates[i], i + 1)
        
        res = []
        n = len(candidates)
        candidates.sort()
        backtrack([], 0, 0)
        return res

        
# @lc code=end

