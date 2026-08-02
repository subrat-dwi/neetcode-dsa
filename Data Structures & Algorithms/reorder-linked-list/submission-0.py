# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        mid = slow

        def reverseLL(head: Optional[ListNode]) -> Optional[ListNode]:
            curr = head
            prev = None

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        second = reverseLL(mid.next)
        mid.next = None
        first = head

        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2


        