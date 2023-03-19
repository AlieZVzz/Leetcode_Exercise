#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def dfs(left,right):
			# 递归的终止条件是两个节点都为空
			# 或者两个节点中有一个为空
			# 或者两个节点的值不相等
            if not left and not right: #都为空，相等
                return True
            if not (left and right):
                return False
            if left.val!=right.val:
                return False
            return dfs(left.left,right.right) and dfs(left.right,right.left)
		# 用递归函数，比较左节点，右节点
        if not root:
            return True
        return dfs(root.left,root.right)



    # def isSymmetric(self, root: 'TreeNode') -> 'bool':

    #     def symmetric(p1, p2):
    #         if p1 and p2:
    #             return (p1.val == p2.val and symmetric(p1.left, p2.right) and 
    #                     symmetric(p1.right, p2.left))
    #         else:
    #             return p1 is p2

    #     if not root:
    #         return True
    #     return symmetric(root.left, root.right)
                
# @lc code=end

