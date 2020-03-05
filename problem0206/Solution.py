from problem0206 import ListNode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        dummy = ListNode(-1)
        pre = head
        cur = head.next
        dummy.next = pre
        while cur is not None:
            pre.next = cur.next
            cur.next = dummy.next
            dummy.next = cur

            cur = pre.next
        return dummy.next
