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
    int maxDepth(TreeNode* root) {
        int lleft= 0;
        int lright = 0;
        if(!root){
            return 0;
        }
        lleft=maxDepth(root->left)+1;
        lright=maxDepth(root->right)+1;
        if(lleft > lright){
            return lleft;
        }
        else{return lright;}
    }
};