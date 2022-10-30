#
# @lc app=leetcode.cn id=1110 lang=python3
#
# [1110] 删点成林
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        forest=[]
        # root_val_overall=root.val
        def dfs(root):
            if not root: return
            
            root.left=dfs(root.left)
            root.right=dfs(root.right)
            if root.val in to_delete:
                # 注意细节:只有非空节点才加入哦
                if root.left: forest.append(root.left)
                if root.right: forest.append(root.right)
                return None    
            else:
                
                return root
        # 不要忘记最后对根节点判断
        root_delete=dfs(root)
        if root_delete is not None: forest.append(root)
        return forest



        
# @lc code=end

