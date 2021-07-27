#TreeNode object meant to be implemented for Recursive Descent parsing

class TreeNode(object):
    def __init__(self, left, right):
        self.val = None
        self.left = left
        self.right = right