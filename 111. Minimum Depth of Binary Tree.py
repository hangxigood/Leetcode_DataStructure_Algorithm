# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.recurive(root, 1)
    
    def recurive(self, root, count):
        if (not root.left) and (not root.right):
            return count
        elif root.left and (not root.right):
            count += 1
            return self.recurive(root.left, count)
        elif root.right and (not root.left):
            count += 1
            return self.recurive(root.right, count)
        else:
            count += 1
            return min(self.recurive(root.left, count), self.recurive(root.right, count))

        