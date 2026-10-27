# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: TreeNode | None) -> TreeNode | None:
        queue = deque([root])
        level = 0

        while queue:
            if level % 2 != 0:
                l = 0
                r = len(queue) - 1


                while l<r:

                    queue[l].val, queue[r].val = queue[r].val, queue[l].val

                    l+= 1
                    r-=1
            for _ in range(len(queue)):

                current = queue.popleft()

                if current.left:

                   queue.append(current.left)

                if current.right:
                   queue.append(current.right)
            level += 1
        return root

        


            
        