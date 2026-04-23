# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node):
        if node is None:
            return 0
        lh = self.dfs(node.left)
        rh = self.dfs(node.right)
        self.dai = max(self.dai,lh+rh)
        return 1+max(lh,rh)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dai=0
        self.dfs(root)
        return self.dai
        