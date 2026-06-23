# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.preorder(q) == self.preorder(p)

    def preorder(self, root):
        if not root:
            return [None]
        return [root.val] + self.preorder(root.left) + self.preorder(root.right)





        