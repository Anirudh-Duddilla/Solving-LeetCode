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
    int flag = 0;
public:
    bool isBalanced(TreeNode* root) {
        height(root);
        if(flag){return false;}
        else{return true;}
    }
    int height(TreeNode* root){
        if(!root){return 0;}
        int lft = 1 + height(root->left);
        int rgt = 1 + height(root->right);
        int dif = max(lft,rgt) - min(lft,rgt);
        // cout << lft << " " << rgt << " " << dif<<endl;
        if(dif > 1){
            flag = 1;
        }
        return max(lft,rgt);
    }
};