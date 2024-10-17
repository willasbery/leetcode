# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def search(root) -> int:
            left = 0 if not root.left else search(root.left)
            right = 0 if not root.right else search(root.right)

            return 1 + max(left, right)

        if root is None:
            return 0

        return search(root)