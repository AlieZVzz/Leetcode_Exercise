#
# @lc app=leetcode.cn id=103 lang=python3
#
# [103] 二叉树的锯齿形层序遍历
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional,List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = []
        queue = [root]
        order = 1
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                tree = queue.pop(0)
                tmp.append(tree.val)
                if tree.left:
                    queue.append(tree.left)
                if tree.right:
                    queue.append(tree.right)
            ans.append(tmp[::order])
            order*=-1
        return ans

# @lc code=end

