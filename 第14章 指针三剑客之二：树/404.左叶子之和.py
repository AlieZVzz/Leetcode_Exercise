#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
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
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        res = 0
        if root.left != None and root.left.left == None and root.left.right == None:
            res+=root.left.val
        return self.sumOfLeftLeaves(root.left)+self.sumOfLeftLeaves(root.right)+res
# @lc code=end
