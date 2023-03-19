#
# @lc app=leetcode.cn id=113 lang=python3
#
# [113] 路径总和 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        stack = [(root, [root.val], targetSum)]
        ans = []
        while stack:
            n, v, t = stack.pop()
            if not n.left and not n.right and n.val==t:
                ans.append(v)
            if n.right:
                stack.append((n.right, v+[n.right.val], t-n.val))
            if n.left:
                stack.append((n.left, v+[n.left.val], t-n.val))
        return ans
# @lc code=end

