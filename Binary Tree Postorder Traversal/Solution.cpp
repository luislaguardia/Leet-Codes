#include <vector>
#include <stack>

using namespace std;

class Solution {
public:
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int> result;
        stack<TreeNode*> stack;
        TreeNode* lastVisitedNode = nullptr;

        while (root != nullptr || !stack.empty()) {
            if (root != nullptr) {
                stack.push(root);
                root = root->left;
            } else {
                TreeNode* peekNode = stack.top();
                if (peekNode->right != nullptr && lastVisitedNode != peekNode->right) {
                    root = peekNode->right;
                } else {
                    result.push_back(peekNode->val);
                    lastVisitedNode = stack.top();
                    stack.pop();
                }
            }
        }

        return result;
    }
};
