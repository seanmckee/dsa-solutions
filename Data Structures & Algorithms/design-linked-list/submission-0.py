class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.prev = None
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = ListNode(0)  # dummy
        self.tail = ListNode(0)  # dummy
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        curr = self.head.next
        for _ in range(index):
            curr = curr.next

        return curr.val

    def addAtHead(self, val: int) -> None:
        node = ListNode(val)

        first = self.head.next

        self.head.next = node
        node.prev = self.head

        node.next = first
        first.prev = node

        self.size += 1


    def addAtTail(self, val: int) -> None:
        node = ListNode(val)

        last = self.tail.prev

        last.next = node
        node.prev = last

        node.next = self.tail
        self.tail.prev = node

        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0

        if index > self.size:
            return

        prev = self.head
        for _ in range(index):
            prev = prev.next

        nxt = prev.next
        node = ListNode(val)

        prev.next = node
        node.prev = prev

        node.next = nxt
        nxt.prev = node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        curr = self.head.next
        for _ in range(index):
            curr = curr.next

        curr.prev.next = curr.next
        curr.next.prev = curr.prev

        self.size -= 1