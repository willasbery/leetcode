# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def bfs(tree: Optional[TreeNode]):
            res = []
            queue = [tree]

            while queue:
                curr = queue.pop(0)
                res.append(curr.val)

                if curr.left: 
                    queue.append(curr.left)
                else:
                    res.append("x")

                if curr.right: 
                    queue.append(curr.right)
                else:
                    res.append("y")

            return res

        if p is None and q is None:
            return True
        elif p is None and q is not None or p is not None and q is None:
            return False
        else:
            return bfs(p) == bfs(q)