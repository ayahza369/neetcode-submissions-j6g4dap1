# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        isBalanced=True
        def dfs(root):
            nonlocal isBalanced
            left,right=0,0
            if root is None:
                return 0
            if root.left:
                left=dfs(root.left)
            if root.right:
                right=dfs(root.right)
            if abs(left-right)>1:
                isBalanced=False
            return 1+max(right,left)
        
          
            
        dfs(root)
        return isBalanced
        #queue=deque([root])
        #right,left=0,0
        #while queue:
            
            #length=len(queue)    
            
            #for _ in range(length):     
                #node=queue.popleft()
                #if node.left:
                    #left+=1
                    #queue.append(node.left)

                
                    
                #if node.right:
                    #right+=1
                    #queue.append(node.right)
            #print(left,right)

            #if abs(right-left)>1:
                #return False
                    

            
            
        #return True
