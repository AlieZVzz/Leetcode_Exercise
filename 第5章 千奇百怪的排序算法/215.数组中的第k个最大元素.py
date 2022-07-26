#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
import heapq
# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort(reverse = True)
        # return nums[k-1]
        heap = []
        for num in nums:
            heapq.heappush(heap, num)
            if len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

# @lc code=end
