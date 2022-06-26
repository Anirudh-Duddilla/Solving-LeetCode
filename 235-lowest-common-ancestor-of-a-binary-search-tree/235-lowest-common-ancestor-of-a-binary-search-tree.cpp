/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
       
        // cout<<(p->val>root->val<q->val);
        if(p->val<root->val && root->val>q->val){
            // cout<<"end"<<endl;
            return lowestCommonAncestor(root->left,p,q);
        }
        if(p->val>root->val &&root->val<q->val){
            // cout<<"chk"<<endl;
            return lowestCommonAncestor(root->right,p,q);
        }
        if(p->val<root->val<q->val){
            // cout<<"ok"<<endl;
            return root;
        }
        return root;
        // TreeNode* cur = root;
        // while (cur){
        //     if(p->val < cur->val && cur -> val > q->val){
        //         cur = cur ->left;
        //     }
        //     else if(p->val > cur->val && cur -> val < q->val){
        //         cur = cur->right;
        //     }
        //     else {return cur;}
        // }
        // return cur;
    }
};