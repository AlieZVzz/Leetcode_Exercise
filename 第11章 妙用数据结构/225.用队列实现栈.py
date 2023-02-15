#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
class MyStack:

    def __init__(self):
        self.major_queue = []
        self.help_queue = []


    def push(self, x: int) -> None:
        # 新元素放入辅助队列的队首
        self.help_queue.append(x)
        # 将主队列的元素加入辅助队列
        while self.major_queue:
            self.help_queue.append(self.major_queue.pop(0))
        # 现在辅助队列元素是和栈的元素排列一致，为了后续方便理解，交换两个队列的内容
        self.major_queue = self.help_queue
        self.help_queue = []


    def pop(self) -> int:
        # 判断是否为空
        if self.empty():
            return None
        # pop移除栈顶元素，相当于移除主队列的队首元素
        return self.major_queue.pop(0)



    def top(self) -> int:
        return self.major_queue[0]


    def empty(self) -> bool:
        if not self.major_queue:
            return True
        return False



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

