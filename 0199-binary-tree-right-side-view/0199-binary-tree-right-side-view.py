# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if not root:
            return []

        self.queue = deque([root])
        result = []

        while self.queue:
            level_size = len(self.queue)

            for i in range(level_size):
                node = self.queue.popleft()

                if i == level_size - 1:
                    result.append(node.val)
                if node.left:
                    self.queue.append(node.left)
                if node.right:
                    self.queue.append(node.right)
        return result


        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        