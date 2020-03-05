class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA = headA
        nodeB = headB
        lenA = self.getListLength(nodeA)
        lenB = self.getListLength(nodeB)
        if lenA > lenB:
            headA = self.moveForward(lenA, lenB, headA)
        else:
            headB = self.moveForward(lenB, lenA, headB)

        while headA is not None and headB is not None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next

        return None

    def getListLength(self, head: ListNode) -> int:
        length = 0
        while head is not None:
            head = head.next
            length = length + 1
        return length

    def moveForward(self, longLength: int, shortLength: int, head: ListNode) -> ListNode:
        delat = longLength - shortLength
        while head is not None and delat > 0:
            delat = delat - 1
            head = head.next
        return head

    def getIntersectionNodeBySet(self, headA: ListNode, headB: ListNode) -> ListNode:
        listNodeSet = set()
        while headA is not None:
            listNodeSet.add(headA)
            headA = headA.next

        while headB is not None:
            if headB in listNodeSet:
                return headB
            headB = headB.next
        return None

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodeA = headA
        nodeB = headB

        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA is not None else headB
            nodeB = nodeB.next if nodeB is not None else headA
        return nodeA
