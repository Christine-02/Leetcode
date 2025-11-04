# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ptrstart = head
        ptrkth = head
        ptrend = head
        count=0


        while(ptrend and ptrend.next):
            count += 1
            ptrend=ptrend.next
        count += 1

        k = k % count
        if k == 0:
            return head

        kth = count-k
        count2=0
        while(count2 != kth-1):
            count2 += 1
            ptrkth=ptrkth.next
        new_head = ptrkth.next
        ptrkth.next = None

        ptrend.next = head

        return new_head
 