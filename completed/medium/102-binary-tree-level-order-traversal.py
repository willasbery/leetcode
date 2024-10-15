# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = []
        queue = [root]
        
        while queue:
            this_level = [] # temp store for this levels values
            
            for i in range(len(queue)):
                node = queue.pop(0) # pop the first item from the queue
                this_level.append(node.val) # add this val to the temp store
                
                # add the children
                if node.left: queue.append(node.left) 
                if node.right: queue.append(node.right)
            
            res.append(this_level)
        
        return res