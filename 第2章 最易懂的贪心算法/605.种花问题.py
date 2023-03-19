#
# @lc app=leetcode.cn id=605 lang=python3
#
# [605] 种花问题
#

# @lc code=start

# 防御式编程思想：在 flowerbed 数组两端各增加一个 0， 这样处理的好处在于不用考虑边界条件，任意位置处只要连续出现三个 0 就可以栽上一棵花。
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        max_flower = 0
        flowerbed = [0]+flowerbed+[0]
        for i in range(1, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                max_flower += 1
                flowerbed[i] = 1
        return max_flower >= n

