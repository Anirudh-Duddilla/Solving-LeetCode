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
    bool isPalindrome(ListNode* head) {
        ListNode* slow = head;
        ListNode* fast = head;
        while(fast ){
            if(!fast->next){break;}
            slow = slow->next;
            fast = fast->next->next;
        }

        ListNode* rev = slow->next;
        fast = slow;
        while(rev){
            slow -> next = rev -> next;
            rev -> next =  fast;
            fast = rev;
            rev = slow -> next;
        }
        ListNode* curr = head;
        rev = fast;
        while(rev){
            // cout<<curr->val<< " " <<rev<<endl;
            // cout<<curr<< " " <<rev<<endl;
            if(curr->val != rev->val){
                return false;
            }
            curr = curr->next;
            rev = rev->next;
        }
        return true;
    }
};