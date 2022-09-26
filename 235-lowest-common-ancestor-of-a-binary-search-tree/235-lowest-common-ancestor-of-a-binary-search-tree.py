# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        curr = root
        
        while curr:
            
            if q.val < curr.val and p.val < curr.val:
                curr = curr.left
            elif q.val > curr.val and p.val > curr.val:
                curr = curr.right
            else:
                return curr