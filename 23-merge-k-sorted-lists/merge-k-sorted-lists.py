# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Base case: if the input list is empty or None, return None
        if not lists or len(lists) == 0:
            return None

        # Loop until we reduce the list of linked lists to one list
        while len(lists) > 1:
            mergedLists = []

            # Process pairs of lists
            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if (i + 1) < len(lists) else None
                mergedLists.append(self.mergeList(l1, l2))

            # Update lists to be the merged lists
            lists = mergedLists

        # The final merged list
        return lists[0]

    def mergeList(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Dummy node to start the merged list
        dummy = ListNode()
        tail = dummy

        # Merge the two lists
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        # Attach any remaining nodes
        tail.next = l1 if l1 else l2

        # Return the merged list starting from dummy's next node
        return dummy.next
        