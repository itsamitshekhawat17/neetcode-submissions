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
        if abs(lh-rh)>=2:
            self.ans= False
        return 1 + max(lh,rh)
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.ans = True
        self.dfs(root)
        return self.ans