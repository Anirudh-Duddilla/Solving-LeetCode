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
    int dia = -1;
public:
    int diameterOfBinaryTree(TreeNode* root) {
        height(root);
        return dia;
    }
    
    int height(TreeNode* root){
        if(!root){
            return -1;
        }
        int lleft = 1+height(root->left);
        cout << "l = " <<lleft <<", "<< root->val;
        int lright = 1+ height(root->right);
        dia = max(dia, (lleft+lright));
        cout<<" r = " << lright <<", "<< root->val<< " d = " << dia << endl;
        return max(lleft, lright);
    }
};