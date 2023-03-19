#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort(reverse = True)
        # return nums[k-1]
        def patition(arr, low, high):
            i = low -1
            pivot = arr[high]
            for j in range(low, high):
                if arr[j]<=pivot:
                    i += 1
                    arr[j],arr[i] = arr[i],arr[j]
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return i+1
        
        low = 0
        high = len(nums)-1
        k = len(nums)-k
        while low<high:
            middle = patition(nums, low, high)
            if middle==k:
                return nums[middle]
            elif middle > k:
                high = middle-1
            else:
                low = middle+1
        return nums[low]
    

# @lc code=end
