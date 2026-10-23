# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root):
        result = []

        def dfs(node):
            if node is None:
                return

            dfs(node.left)             # 1. Visit left subtree
            result.append(node.val)    # 2. Add root value
            dfs(node.right)            # 3. Visit right subtree

        dfs(root)
        return result