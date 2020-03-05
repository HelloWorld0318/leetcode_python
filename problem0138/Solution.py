# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        cur = head

        while cur is not None:
            node = Node(cur.val)
            node.next = cur.next
            cur.next = node
            cur = node.next

        cur = head
        while cur is not None:
            if cur.random is not None:
                cur.next.random = cur.random.next
            cur = cur.next.next

        dummy = Node(-1)
        newListNode = dummy
        cur = head
        while cur is not None:
            newListNode.next = cur.next
            newListNode = newListNode.next

            cur.next = cur.next.next
            cur = cur.next
        return dummy.next
