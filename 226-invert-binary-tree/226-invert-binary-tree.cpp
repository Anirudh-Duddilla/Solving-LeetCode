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
    TreeNode* invertTree(TreeNode* root) {
        if(!root){
            return root;
        }
        TreeNode* dummy = root;
        TreeNode* temp = nullptr;
        invertTree(dummy->left);
        invertTree(dummy->right);
        temp = dummy->right;
        dummy->right = dummy->left;
        dummy->left = temp;
        
        // TreeNode* lft = invertTree(dummy->left);
        // TreeNode* rgt = invertTree(dummy->right);
        // temp = rgt;
        // rgt = lft;
        // lft = temp;
        // dummy->left = lft;
        // dummy->right = rgt;
        
        return root;
    }
};