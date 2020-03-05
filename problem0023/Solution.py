from _ast import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if lists is None or len(lists) == 0:
            return None
        return self.mergeLists(lists, 0, len(lists) - 1)

    def mergeLists(self, lists: List[ListNode], start: int, end: int):
        if start == end:
            return lists[start]
        mid = (start + end) // 2
        left = self.mergeLists(lists, start, mid)
        right = self.mergeLists(lists, mid + 1, end)
        return self.mergeList(left, right)

    def mergeList(self, headA: ListNode, headB: ListNode) -> ListNode:
        dummy = ListNode(-1)
        node = dummy

        while headA is not None or headB is not None:
            if headA is None or (headB is not None and headB.val < headA.val):
                node.next = headB
                headB = headB.next
            else:
                node.next = headA
                headA = headA.next
            node = node.next
        return dummy.next
