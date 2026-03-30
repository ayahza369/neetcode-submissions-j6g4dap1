# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def helper(root,subRoot):
            if not(root or subRoot):
                return True
            if not(root and subRoot):
                return False
            elif root.val!=subRoot.val:
               return False
            left=helper(root.left,subRoot.left)
            right=helper(root.right,subRoot.right)
            return left and right
        if root:
            if helper(root,subRoot):
               return True
            else:
                return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot)
        return subRoot==None