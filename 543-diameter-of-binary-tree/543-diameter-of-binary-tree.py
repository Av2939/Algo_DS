# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        
        self.diameter = 0
        self.dfs(root)
        return self.diameter
        
        
    
    def dfs(self, node):
        
        if node is None:
            return 0
        
        left_max = self.dfs(node.left)
        right_max = self.dfs(node.right)
        
        self.diameter = max(self.diameter, left_max + right_max)
        
        return max(left_max, right_max) + 1
        