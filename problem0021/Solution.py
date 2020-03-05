class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        node = dummy
        while l1 is not None or l2 is not None:
            if l1 is None or (l2 is not None and l2.val < l1.val):
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        return dummy.next
