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
    vector<int> preorderTraversal(TreeNode* root) {
        std::stack<TreeNode*> nodestck{};
        vector<int> res{};
        TreeNode* curr = root;

        if(nodestck.empty() && root){
            nodestck.push(curr);
        }
        while(!nodestck.empty()){
            curr = nodestck.top();
            res.push_back(curr->val);
            nodestck.pop();
            if(curr->right){nodestck.push(curr->right);}
            if(curr->left){nodestck.push(curr->left);}
        }
        return res;
    }
};