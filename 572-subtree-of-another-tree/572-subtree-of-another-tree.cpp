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
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        if(!root&&!subRoot){ cout<<0;return true;}
        else if(! root ||!subRoot){return false;}
        
        return sametree(root,subRoot)||isSubtree(root->left,subRoot)||isSubtree(root->right,subRoot);
    }
    
    bool sametree(TreeNode* p, TreeNode* q){
        // cout <<p->val<<" " <<q->val<<endl;
        if(!p && !q){return true;}
        if(!p || !q){return false;}
        if(p->val != q->val){
            return false;
        }
        return(sametree(p->left,q->left)&&sametree(p->right,q->right));
    }
};