# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_tree(self,node,subnode):
        if node is None and subnode is None:
            return True 
        elif node is None or subnode is None:
            return False
        elif node.val!=subnode.val:
            return False
        return self.check_tree(node.left,subnode.left) and self.check_tree(node.right, subnode.right)

    def dfs(self,node,subnode):
        if node is None:
            return False
        if self.check_tree(node,subnode):
            return True
        return self.dfs(node.left,subnode) or self.dfs(node.right,subnode)
        

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs(root,subRoot)
      
        