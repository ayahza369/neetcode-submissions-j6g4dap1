# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p,q):
            if not (p or q):
                return  True
            if not (p and q):
                return False
            if not (p or q):
                return False
            if p.val!=q.val:
                return False
            
            else:
                right=dfs(p.right,q.right)
                left=dfs(p.left,q.left)
            return left and right
        return dfs(p,q)