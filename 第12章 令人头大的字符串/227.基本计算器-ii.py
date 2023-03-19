#
# @lc app=leetcode.cn id=227 lang=python3
#
# [227] 基本计算器 II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        n = len(s)
        # pre_sign 初始为加号
        pre_sign = '+'
        num = 0
        stack = []

        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord('0')
    
            # 注意 i ==  n - 1 这个条件，这里表示到达末尾
            # 这里是根据 pre_sign 来确定其跟在后面的数字的计算方式
            # 代码中，遇到下一个运算符时，才会处理前面的运算，本题当到达末尾时，不会再出现单独的运算符，所以需要进行额外判断，到达末尾同样处理前面的运算
            if not s[i].isdigit() and s[i] != ' ' or i == n - 1:
                if pre_sign == '+':
                    stack.append(num)
                elif pre_sign == '-':
                    stack.append(-num)
                elif pre_sign == '*':
                    stack.append(stack.pop() * num)
                else:
                    # stack.append(stack.pop() // num)
                    # 这里就是开篇提的小坑, python 中 // 是向下取整，当出现负数时，这里的结果就会出现偏差，所以直接用 / 运算后取整数部分
                    stack.append(int(stack.pop() / num))
                #  更新当前的运算符
                pre_sign = s[i]
                num = 0
        
        ans = 0
        while stack:
            ans += stack.pop()
        
        return ans
# @lc code=end

