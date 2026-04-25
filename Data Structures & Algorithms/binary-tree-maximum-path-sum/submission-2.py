# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node , path_sum):
        if node is None:
            return 0
        lh = max(0,self.dfs(node.left,path_sum))
        rh = max(0,self.dfs(node.right,path_sum))
        self.path_sum = max(self.path_sum , node.val+lh+rh)
        return node.val+max(lh,rh)
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.path_sum = float('-inf')
        self.dfs(root,self.path_sum)
        return self.path_sum

        
        