#
# @lc app=leetcode.cn id=347 lang=python3
#
# [347] 前 K 个高频元素
#

# @lc code=start


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for i in range(0, len(nums)):
            if nums[i] in dict:
                dict[nums[i]] +=1
            else:
                dict[nums[i]] = 1
        nums = sorted(dict.items(),key=lambda x:x[1], reverse=True)
        return [i for i,_ in nums[:k]]

# @lc code=end

