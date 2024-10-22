class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        
        num_nodes = [0]

        def dfs(root):
            if not root:
                return(0, 0)
            
            N_left, summ_l = dfs(root.left)
            N_right, summ_r = dfs(root.right)

            N = 1 + N_left + N_right
            summ = root.val + summ_l + summ_r
            avg = summ // N

            if root.val == avg:
                num_nodes[0] += 1

            return (N, summ)

        dfs(root)
        return num_nodes[0]
