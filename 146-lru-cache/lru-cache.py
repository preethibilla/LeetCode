class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hashmap to store key and its corresponding node
        self.head = Node(0, 0)  # Dummy head node
        self.tail = Node(0, 0)  # Dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def insert(self, node):
        """ Add new node right after head. """
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node):
        """ Remove an existing node from the linked list. """
        prev = node.prev
        new = node.next
        prev.next = new
        new.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])  # Remove the node from its current position
            self.insert(self.cache[key])  # Insert the node at the head (most recently used)
            return self.cache[key].value  # Return the value of the node
        return -1  # Key not found, return -1
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])  # Remove the existing node if it exists
        self.cache[key] = Node(key, value)  # Create a new node and add it to the HashMap
        self.insert(self.cache[key])  # Insert the new node at the head (most recently used)
        if len(self.cache) > self.capacity:
            # If cache exceeds capacity, remove the least recently used (LRU) node
            lru = self.tail.prev  # The node previous to the tail is the least recently used
            self.remove(lru)  # Remove the LRU node from the linked list
            del self.cache[lru.key]  # Delete the LRU node from the HashMap


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)