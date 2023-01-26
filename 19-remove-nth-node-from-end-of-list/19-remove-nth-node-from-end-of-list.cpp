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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* lst = head->next;
        ListNode* fst = head;
        n-=1;
        ListNode* tmp = new ListNode;
        tmp -> next = fst;
        while(lst){
            if(n){
                lst = lst->next;
                if(head->next == lst && !lst){
                    head =nullptr; 
                    return head;}
                n-=1;
                continue;
            }
            tmp = tmp->next;
            fst = fst->next;
            cout << n<< " "<<fst->val<<endl;
            lst = lst->next;
        }
        // cout << n<< " "<<fst->val<<endl;
        // fst ->next = fst ->next ->next;
        if(fst == head){
            head = head->next;
            // cout << n<< " "<<head->val<<endl;
            }
        else{
            tmp ->next = fst ->next;
            }
        return head;
    }
};