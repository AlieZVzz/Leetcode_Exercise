#
# @lc app=leetcode.cn id=932 lang=python3
#
# [932] 漂亮数组
#

# @lc code=start
from typing import List
class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        memo = {1 : [1]}
        def f(N):
            if N not in memo:
                memo[N] = [2 * x - 1 for x in f((N + 1) // 2)] + [2 * x for x in f(N // 2)]
            return memo[N]
        return f(n)


# @lc code=end

