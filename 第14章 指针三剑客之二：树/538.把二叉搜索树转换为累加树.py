#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
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
    def __init__(self) -> None:
        self.num = 0
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root!=None:
            self.convertBST(root.right)
            root.val = root.val+self.num
            self.num = root.val
            self.convertBST(root.left)
            return root
        return None

# @lc code=end

