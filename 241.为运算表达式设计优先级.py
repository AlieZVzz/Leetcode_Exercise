#
# @lc app=leetcode.cn id=241 lang=python3
#
# [241] 为运算表达式设计优先级
#

# @lc code=start


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

# @lc code=end

