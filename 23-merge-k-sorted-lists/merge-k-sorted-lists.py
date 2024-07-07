# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Define a min-heap
        min_heap = []

        # Initialize the heap with the head of each linked list
        for i in range(len(lists)):
            if lists[i]:
                # Push tuple of (node value, index of the list, node)
                heappush(min_heap, (lists[i].val, i, lists[i]))

        # Dummy node to serve as the starting point of the merged linked list
        dummy = ListNode()
        current = dummy

        # Process the heap until it is empty
        while min_heap:
            # Extract the smallest node from the heap
            val, i, node = heappop(min_heap)

            # Add the smallest node to the merged linked list
            current.next = node
            current = current.next

            # If there is a next node in the same list, push it to the heap
            if node.next:
                heappush(min_heap, (node.next.val, i, node.next))

        # Return the merged linked list, starting from the dummy node's next
        return dummy.next