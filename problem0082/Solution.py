# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        node = head.next

        if node.val == head.val:
            while node is not None and node.val == head.val:
                node = node.next
            return self.deleteDuplicates(node)
        else:
            head.next = self.deleteDuplicates(node)
            return head
