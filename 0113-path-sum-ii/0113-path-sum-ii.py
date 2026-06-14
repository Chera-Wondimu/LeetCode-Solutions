# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(node, target, path):
            if not node:
                return
            path.append(node.val)
            target -= node.val
            if not node.left and not node.right and target == 0:
                res.append(path[:]) 
            dfs(node.left, target, path)
            dfs(node.right, target, path)
            path.pop()  
        dfs(root, targetSum, [])
        return res