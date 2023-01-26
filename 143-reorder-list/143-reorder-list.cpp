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
    void reorderList(ListNode* head) {
        ListNode* prev = head;
        ListNode* curr = prev->next;
        ListNode* rehead = prev;
        while(prev->next && prev->next->next){
            if(!curr->next){
                curr->next = prev->next;
                prev->next = curr;
                rehead->next = nullptr;
                prev = curr->next;
                curr = prev->next;
                rehead = prev;
                cout << prev->val<< endl;
            }
            if(prev==rehead && !rehead->next){break;}
            rehead = curr;
            curr = curr->next;
        }
    }
};