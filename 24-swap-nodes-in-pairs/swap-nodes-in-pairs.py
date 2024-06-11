# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temphead = ListNode(0,head)
        prev = temphead
        curr = head
        while curr and curr.next:
        #saving the next pair
            nextSwapPair = curr.next.next
        # node to be swapped with the current node
            second = curr.next
        #swap nodes
        #second node points to the current node
            second.next = curr
        #code node is pointing to the nextPair
            curr.next = nextSwapPair
        #prev node is pointing to the second
            prev.next = second
        #move the position of the pointers
            prev =  curr
            curr = nextSwapPair
        #return the new head of the list which is the next node of the temphead
        return temphead.next
        