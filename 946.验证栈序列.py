#
# @lc app=leetcode.cn id=946 lang=python3
#
# [946] 验证栈序列
#

# @lc code=start
from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        st, j = [], 0
        for x in pushed:
            st.append(x)
            while st and st[-1] == popped[j]:
                st.pop()
                j+=1
        return len(st)==0
# @lc code=end

