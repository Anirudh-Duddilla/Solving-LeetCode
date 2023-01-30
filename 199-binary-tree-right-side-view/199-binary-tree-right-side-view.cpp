/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> res = {};
        TreeNode* curr = root;
        queue<TreeNode* > q ={};
        q.push(curr);
        while(!q.empty()){
            TreeNode* rgtside = nullptr;
            int qlen = q.size();
            for(int i=0; i<qlen; i++){
                TreeNode* frnt = q.front();
                q.pop();
                if (frnt){
                    rgtside = frnt;
                    q.push(frnt->left);
                    q.push(frnt->right);
                }
            }
            if(rgtside){res.push_back(rgtside->val);}
        }
        return res;
    }
};