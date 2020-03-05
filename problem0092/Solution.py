class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None or head.next is None or n == m:
            return head

        preHead = None
        result = head
        changeLen = n - m + 1

        while head is not None and m - 1 > 0:
            preHead = head
            head = head.next
            m = m - 1

        modifyListTail = head
        newHead = None

        while head is not None and changeLen > 0:
            next = head.next
            head.next = newHead
            newHead = head

            changeLen = changeLen - 1
            head = next
        modifyListTail.next = head

        if preHead is not None:
            preHead.next = newHead
        else:
            result = newHead
        return result
