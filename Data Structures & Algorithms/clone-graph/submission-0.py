"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        cloned = {node: Node(node.val)}
        queue = deque([node])

        while queue:
            n = queue.popleft()

            for nei in n.neighbors:
                if nei not in cloned:
                    queue.append(nei)
                    cloned[nei] = Node(nei.val)
                cloned[n].neighbors.append(cloned[nei])

        return cloned[node]