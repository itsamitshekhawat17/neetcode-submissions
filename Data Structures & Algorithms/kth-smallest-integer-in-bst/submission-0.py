# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node):
        if node is None:
            return None
        self.dfs(node.left)
        self.ans.append(node.val)
        self.dfs(node.right)
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans = []
        self.dfs(root)
        return self.ans[k-1]
        
        