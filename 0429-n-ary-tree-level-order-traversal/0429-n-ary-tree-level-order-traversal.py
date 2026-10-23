"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    from collections import deque
    def levelOrder(self, root: 'Node') -> List[List[int]]:

        if not root:
            return []
        
        queue = deque([root])
        res = []

        while queue:
            level = []

            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                for child in node.children:
                    if child is not None:
                        queue.append(child)
            
            res.append(level)

        return res
        
        