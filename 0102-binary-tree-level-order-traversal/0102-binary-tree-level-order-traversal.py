# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        if not root:
            return []
        self.queue = deque([root])
        result = []

        while self.queue:
            level = []
            level_size = len(self.queue)

            for i in range(level_size):
                node = self.queue.popleft()
                level.append(node.val)

                if node.left:
                    self.queue.append(node.left)
                if node.right:
                    self.queue.append(node.right)

            result.append(level)
        return result

                      