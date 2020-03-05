class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if head is None or head.next is None:
            return head
        lessHead = ListNode(-1)
        lessPtr = lessHead
        moreHead = ListNode(-1)
        morePtr = moreHead

        while head is not None:
            if head.val < x:
                lessPtr.next = head
                lessPtr = lessPtr.next
            else:
                morePtr.next = head
                morePtr = morePtr.next
            head = head.next

        morePtr.next = None
        lessPtr.next = moreHead.next
        return lessHead.next
