/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        int la = lenLL(headA);
        int lb = lenLL(headB);
        ListNode* curA = headA;
        ListNode* curB = headB;
        while(curA != curB){
            if(la != lb && la > lb){
                curA = curA->next;
                la -= 1;
                continue;
            }
            else if(la !=lb && la < lb){
                curB = curB->next;
                lb -= 1;
            }
            else{
                curA = curA -> next;
                curB = curB -> next;

            }
        }
        return curA;
        
    }
    int lenLL(ListNode* head){
        int count = 0;
        while(head){
            count ++;
            head = head->next;
        }
        return count;
    }
};