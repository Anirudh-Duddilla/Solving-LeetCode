/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* middleNode(ListNode* head) {
        ListNode* fst = new ListNode();
        fst -> next = head;
        ListNode* scd = fst;
        while(fst != nullptr){
            fst = fst -> next;
            scd = scd->next->next;
            if(scd == nullptr){
                break;
            }
            else if(scd -> next == nullptr){
                return fst->next;
            }
        }
        return fst;
    }
};