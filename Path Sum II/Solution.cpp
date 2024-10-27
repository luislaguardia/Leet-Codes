class Solution {
public:
    vector<vector<int>> result;
    
    void dfs(TreeNode* node, int targetSum, vector<int>& path) {
        if (!node) return;
        
        path.push_back(node->val);
        targetSum -= node->val;
        
        if (!node->left && !node->right && targetSum == 0) {
            result.push_back(path);
        }
        
        dfs(node->left, targetSum, path);
        dfs(node->right, targetSum, path);
        
        path.pop_back();
    }
    
    vector<vector<int>> pathSum(TreeNode* root, int targetSum) {
        vector<int> path;
        dfs(root, targetSum, path);
        return result;
    }
};
