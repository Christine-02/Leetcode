# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        slow=head
        fast=head

        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next

        if fast:  
            slow = slow.next

        slow = self.reverse(slow)

        first = head
        second = slow
        while(second and first):
            if (first.val != second.val):
                return False
            first = first.next
            second = second.next
            
        
        return True
        
        
        
    def reverse(self,head):
        temp = head
        prev = None
        while(temp):
            new = temp.next
            temp.next = prev
            prev = temp
            temp = new
        return prev

        




