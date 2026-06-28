# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        curr1 = head
        curr2 = head

        if not head:
            return None

        while n-1 > 0:
            curr1 = curr1.next
            n-=1

        while curr1.next:
            prev = curr2
            curr1 = curr1.next
            curr2 = curr2.next
        if not prev:
            return head.next
        prev.next = curr2.next

        return head



        

        


        