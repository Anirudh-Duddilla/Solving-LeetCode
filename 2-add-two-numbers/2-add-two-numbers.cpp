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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sum = 0;
        int cf = 0;
        // ListNode temp_node = new ListNode();
        ListNode* temp = new ListNode;
        ListNode* res = temp;

        while(l1 || l2){
            temp->next = new ListNode;
            if(l1 && l2){
                sum = l1->val + l2->val + cf;
                l1 = l1->next;
                l2 = l2->next;
            }
            else if(!l1 && l2){
                sum = l2 -> val +cf;
                l2 = l2 ->next;
            }
            else if(l1 && !l2){
                sum = l1 ->val + cf;
                l1 = l1->next;
            }
            if(sum>9){
                cf = sum / 10;
                temp->next->val = sum%10;
            }
            else{
                cf = 0;
                temp->next->val = sum;
            }

            // temp -> next = temp_nd;
            temp = temp->next;
            cout<<temp->val<<" "<<temp<<endl;
            // temp_nd = nullptr;
        }
        if(cf){
            temp->next = new ListNode;
            temp ->next ->val = temp -> next-> val + cf;
            temp = temp->next;
        }
        return res->next;
    }
};