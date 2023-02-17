def FindKthToTail(self, head, k):
    fast = slow = head
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next
    while fast:
        slow, fast = slow.next, fast.next
    return slow