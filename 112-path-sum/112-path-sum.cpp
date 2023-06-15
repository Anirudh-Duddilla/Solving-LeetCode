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
    bool flag = false;
    int sum = 0;
    bool hasPathSum(TreeNode* root, int targetSum) {
        
        TreeNode* curr = root;
        while(!flag){
            if(!curr){ return flag;}
            sum = sum + curr->val;
            hasPathSum(curr->left, targetSum);
            hasPathSum(curr->right, targetSum);
            if(!curr -> left && !curr->right){
                if(sum == targetSum){
                    flag = true;
                    return flag;
                }
            }
            sum = sum - curr->val;           
            return flag;
        }
        return flag;
    }
};