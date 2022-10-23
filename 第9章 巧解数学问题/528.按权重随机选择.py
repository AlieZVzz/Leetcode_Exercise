#
# @lc app=leetcode.cn id=528 lang=python3
#
# [528] 按权重随机选择
#

# @lc code=start
from typing import List
import random
from bisect import bisect_left
from itertools import accumulate
class Solution:

    def __init__(self, w: List[int]):
        self.pre = list(accumulate(w))
        self.total = sum(w)

    def pickIndex(self) -> int:
        x = random.randint(1, self.total)
        return bisect_left(self.pre, x)




# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# @lc code=end

