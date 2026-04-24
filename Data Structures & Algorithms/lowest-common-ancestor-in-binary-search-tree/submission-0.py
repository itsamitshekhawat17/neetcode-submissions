# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def dfs(self,node,p,q):
        if node is None:
            return None
        while node:
            if p.val<node.val and q.val<node.val:
                node = node.left
            elif p.val>node.val and q.val>node.val:
                node = node.right
            else:
                return node
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root,p,q)
        
        