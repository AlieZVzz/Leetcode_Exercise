#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        res = cur = ListNode(-1)
        while list1 and list2:
            if list1.val>list2.val:
                cur.next = list2
                list2 = list2.next

            else:
                cur.next = list1
                list1 = list1.next
            cur = cur.next
        cur.next = list1 if list1 else list2
        # 返回哑节点后面的链表节点
        return res.next

# @lc code=end

