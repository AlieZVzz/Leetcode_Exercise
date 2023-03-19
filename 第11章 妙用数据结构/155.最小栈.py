#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self) -> None:
        self.datastack = []    # 数据栈
        self.sortedstack = []  # 有序栈（栈底最大，栈顶最小，有 <= 栈顶的元素才进行push）


    def push(self, val: int) -> None:
        self.datastack.append(val)
        # --有序栈
        # ----如果为空 则 push
        # ----如果val 不大于 当前栈顶 则 push
        if not self.sortedstack or self.sortedstack[-1] >= val:
            self.sortedstack.append(val) 

    def pop(self) -> None:
        # 数据栈的栈顶如果与 有序栈的栈顶相等， 那么都出栈
        if self.datastack[-1] == self.sortedstack[-1]:
            self.sortedstack.pop()
        self.datastack.pop()

    def top(self) -> int:
        return self.datastack[-1]

    def getMin(self) -> int:
        return self.sortedstack[-1]




# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

