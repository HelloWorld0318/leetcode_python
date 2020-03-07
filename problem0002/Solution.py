class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0

        dummy = ListNode(-1)
        cur = dummy

        while carry > 0 or l1 is not None or l2 is not None:
            valueL1 = l1.val if l1 is not None else 0
            valueL2 = l2.val if l2 is not None else 0

            curValue = (valueL1 + valueL2 + carry) % 10
            carry = (valueL1 + valueL2 + carry) // 10

            cur.next = ListNode(curValue)

            cur = cur.next

            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
        return dummy.next
