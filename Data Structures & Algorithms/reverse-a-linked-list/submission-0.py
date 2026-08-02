# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        i = head
        k = head

        if not head or not head.next:
            return head

        while k.next:
            j = k.next
            k.next = j.next
            j.next = i
            i = j

        return i