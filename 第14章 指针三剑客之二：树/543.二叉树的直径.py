#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
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
    def __init__(self):
        self.max = 0
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

       
        def depth(root: Optional[TreeNode]) -> int:
            if not root:
                return 0
            l = depth(root.left)
            r = depth(root.right)
            '''每个结点都要去判断左子树+右子树的高度是否大于self.max，更新最大值'''
            self.max = max(self.max, l+r)
            
            # 返回的是高度
            return max(l, r) + 1

        depth(root)
        
        return self.max
        
    
# @lc code=end

