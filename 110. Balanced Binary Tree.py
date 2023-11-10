# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        if root:
            if not root.left or not root.right:
                if not root.left and root.right:
                    if root.right.left or root.right.right:
                        return False
                elif not root.right and root.left:
                    if root.left.left or root.left.right:
                        return False
            else:
                self.isBalanced(root.left)
                self.isBalanced(root.right)
                
        return True