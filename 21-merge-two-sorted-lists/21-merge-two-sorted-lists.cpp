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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* l = new ListNode;
        ListNode* e = l;
        ListNode* p = nullptr;
        // cout << "l = " << l;
        // l->next = p;
        // cout << " p = " << p << endl;
        while(list1 ||list2){
            
            if(!list1){
                p = list2;
                cout << " p = " << p->val << endl;
                e -> next= p;
                e = e->next;
                break;}
            else if(!list2){
                p = list1; 
                cout << " p = " << p->val << endl;
                e -> next= p;
                e = e->next;
                break;}
            else if(list1->val >= list2->val){
                p = list2;
                list2 = list2 -> next;
                cout << " p = " << p->val << endl;
            }
            else{
                p = list1;
                list1 = list1->next;
                cout << " p = " << p->val << endl;
            }
            e -> next= p;
            e = e->next;
        }
        // cout << " l = " << l->next << endl;

        return l->next;
    }
};