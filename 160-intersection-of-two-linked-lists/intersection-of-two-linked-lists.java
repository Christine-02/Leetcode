/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
       ListNode pointera = headA;
       ListNode pointerb = headB;
        while (pointera != pointerb)
        {
            pointera = (pointera != null)? pointera.next : headB;
             pointerb = (pointerb != null)? pointerb.next : headA;
        }

       return pointera;
    }
}