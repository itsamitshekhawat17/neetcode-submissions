# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,node,level):
        if node is None:
            return []
        if len(self.ans)==level:
            self.ans.append(node.val)
        self.dfs(node.right,level+1)
        self.dfs(node.left,level+1)

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        self.ans = []
        self.dfs(root,0)
        return self.ans