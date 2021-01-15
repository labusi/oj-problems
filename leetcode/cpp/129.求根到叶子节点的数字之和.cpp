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
    int sumNumbers(TreeNode* root) {
        int res = 0;
        int parent_val = 0;
        dfs(root, parent_val, res);
        return res;
    }

    /**
     * @param root 当前节点
     * @param  parent_val 不包含当前节点时的值
     * @param res 最终答案
     */
    void dfs(TreeNode* root, int parent_val, int &res) {
        if(root == nullptr)
            return;
        if(root->left == nullptr && root->right == nullptr) { // 叶子
            res += (parent_val * 10 + root->val);
        }

        parent_val = parent_val * 10 + root->val;
        dfs(root->left, parent_val, res);
        dfs(root->right, parent_val, res);
    }
};
