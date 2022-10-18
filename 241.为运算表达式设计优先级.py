#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#

# @lc code=start

from typing import List
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]
        res = []
        for i, char in enumerate(expression):
            if char in ['+','-','*']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if char =='+':
                            res.append(l+r)
                        elif char == '-':
                            res.append(l-r)
                        elif char =='*':
                            res.append(l*r)
        return res

    # 分解：按运算符分成左右两部分，分别求解
    # 解决：实现一个递归函数，输入算式，返回算式解
    # 合并：根据运算符合并左右两部分的解，得出最终解

# @lc code=end

