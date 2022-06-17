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
    ListNode* reverseList(ListNode* head) {
        ListNode* rev_head = nullptr;
        while(head){
            ListNode* temp = new ListNode;
            temp -> val = head -> val;
            if(rev_head == nullptr){
                rev_head = temp;
            }
            else{
                temp -> next = rev_head;
                rev_head = temp;
            }
            head = head->next;
        }
        return rev_head;
    }
};