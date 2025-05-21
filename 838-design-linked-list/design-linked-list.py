class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        
        current = self.head
        position = 0
        
        # Move to the index-th node
        while position < index:
            current = current.next
            position += 1
            
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            # Traverse to the last node
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
            return

        new_node = Node(val)
        current = self.head
        position = 0

        # Move to the node just before the index-th position
        while position < index - 1:
            current = current.next
            position += 1

        new_node.next = current.next
        current.next = new_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            position = 0

            # Move to the node just before the index-th node
            while position < index - 1:
                current = current.next
                position += 1

            current.next = current.next.next

        self.size -= 1
        

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)