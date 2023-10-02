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
    int pairSum(ListNode* head) {
        ListNode* fast = head;
        ListNode* late = head;
        int max_sum = 0;
        std:map<int, int> sum_map;
        int cnt = 0;
        while(fast){
            sum_map[cnt] = late->val;
            // cout<<"late val "<<late->val<<" fast val "<<fast->val<<" map["<<cnt<<"]"<<endl;
            late = late->next;
            fast = fast->next->next;
            cnt +=1;
        }
        cout<<"exit fast "<<cnt<<endl;
        while(late){
            cnt -=1;
            max_sum = max(max_sum, sum_map[cnt]+late->val);
            // cout<<"late val "<<late->val<<" sum "<<max_sum<<" map["<<cnt<<"]"<<endl;
            late = late->next;
        }
        return max_sum;
    }
    
};