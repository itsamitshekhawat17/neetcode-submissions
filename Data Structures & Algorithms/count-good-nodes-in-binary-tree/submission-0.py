# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node,maxi):
        if node is None:
            return 0
        count = 0
        if node.val>=maxi:
            count = 1
            maxi=node.val
        lh = self.dfs(node.left,maxi)
        rh = self.dfs(node.right,maxi)
        return count+lh+rh
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root,float('-inf'))
      
        