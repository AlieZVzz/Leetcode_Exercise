#
# @lc app=leetcode.cn id=226 lang=python3
#
# [226] 翻转二叉树
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
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def reverse(root: Optional[TreeNode]):
            if root is None:
                return
            temp = root.left
            root.left = root.right
            root.right = temp
            reverse(root.left)
            reverse(root.right)
        reverse(root)
        return root
        
# @lc code=end

