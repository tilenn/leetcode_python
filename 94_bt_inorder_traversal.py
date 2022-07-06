# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def traverse_inorder(node, arr):
    if node:
        arr = traverse_inorder(node.left, arr)
        arr.append(node.val)
        arr = traverse_inorder(node.right, arr)
    return arr


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return traverse_inorder(root, [])
