# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs(self,node,maxi_path):
        if node is None:
            return 0
        lh = self.dfs(node.left,self.maxi_path)
        if lh<0:
            lh = 0 
        rh = self.dfs(node.right,self.maxi_path) 
        if rh<0:
            rh = 0
        self.maxi_path = max(self.maxi_path , node.val+lh+rh)
        return node.val + max(lh,rh)
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi_path = float('-inf')
        self.dfs(root,self.maxi_path)
        return self.maxi_path
        