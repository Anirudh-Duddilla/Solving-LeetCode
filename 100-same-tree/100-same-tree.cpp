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
    int flag = 0;
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if(!p && !q){flag=1;return true;}
        else if((!p && q) || (p && !q)||(p->val!=q->val)){flag = 0; return false;}
        traverse(p,q);
        if(flag){return true;}
        else{return false;}
    }
    void traverse(TreeNode* p, TreeNode* q){
        if(!p && !q){return;}
        else if((!p && q) || (p && !q)){ flag = 0; return;}
        flag = check(p->val,q->val);
        traverse(p->left, q->left);
        if(!flag){return;}
        traverse(p->right, q->right);
        return;
    }
    int check(int a, int b){
        if(a==b){return 1;}
        else{return 0;}
    }
};