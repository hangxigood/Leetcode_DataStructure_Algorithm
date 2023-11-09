# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        self.Traversal(root, result)
        return result
    
    def Traversal(self, root, result):
        if root:
            self.Traversal(root.left, result)
            result.append(root.val)
            self.Traversal(root.right, result)
        


