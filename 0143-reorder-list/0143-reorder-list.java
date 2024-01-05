/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) {
            return;
        }
        
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        ListNode prev = null, curr = slow, temp;
        while (curr != null) {
            temp = curr.next;
            curr.next = prev;
            prev = curr;
            curr = temp;
        }
        ListNode cur = head;
        while(cur!=null){
            System.out.println(cur.val);
            cur = cur.next;
        }
        ListNode first = head, second = prev;
        while (second.next != null) {
            temp = first.next;
            first.next = second;
            second = second.next;
            // System.out.println(second.next);
            first.next.next = temp;
            first = temp;
        }
        
        
    }
}