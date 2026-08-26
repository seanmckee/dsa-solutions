# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val=val)
        
        node = root
        prev = None

        while node is not None:
            prev = node
            if val > node.val:
                node = node.right
            elif val < node.val:
                node = node.left 
        if val > prev.val:
            prev.right = TreeNode(val=val)
        elif val < prev.val:
            prev.left = TreeNode(val=val)
        return root