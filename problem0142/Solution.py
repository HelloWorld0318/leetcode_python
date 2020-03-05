class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        listNodeSet = set()
        while head is not None:
            if head in listNodeSet:
                return head
            listNodeSet.add(head)
            head = head.next
        return None

    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return None
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                meetNode = slow
                while head != meetNode:
                    head = head.next
                    meetNode = meetNode.next
                return head
        return None
