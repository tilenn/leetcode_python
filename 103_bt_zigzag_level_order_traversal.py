# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = collections.deque()
        queue.append(root)

        result = []
        f = 1
        while queue:
            n = len(queue)
            tmp = []

            for i in range(n):
                node = queue.popleft()
                if node:
                    tmp.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if tmp:
                result.append(tmp[::f])
                f = f * -1

        return result
