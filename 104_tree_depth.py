# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def get_tree_depth(node):
    if node:
        return 1 + max(get_tree_depth(node.left), get_tree_depth(node.right))
    return 0


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return get_tree_depth(root)
