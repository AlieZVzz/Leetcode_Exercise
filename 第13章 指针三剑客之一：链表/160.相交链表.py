#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        nodeA = headA
        nodeB = headB
        while nodeA != nodeB:
            if nodeA != None:
                nodeA = nodeA.next
            else:
                nodeA = headB
            
            if nodeB != None:
                nodeB = nodeB.next
            else:
                nodeB = headA
        return nodeA
        
# @lc code=end

