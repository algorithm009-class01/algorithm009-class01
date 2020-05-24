def while_loop(l1, l2):
    # Construct a new list p = ListNode()
    # Have two pointer, p1 pointing to the head of l1, p2 pointing to the head of l2
    # Compare two pointers one at a time:
    # if p1.val < p2.val:
    #     add p1 to p
    #     p1 = p1.next
    # else:
    #     add p2 to p
    #     p2 = p2.next
    # If one list has no more element, simply append the other to p
        head = p = ListNode()
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val <= p2.val:
                p.next = p1
                p1 = p1.next
            else:
                p.next = p2
                p2 = p2.next
            p = p.next
        p.next = p1 or p2
        return head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        return while_loop(l1, l2)
