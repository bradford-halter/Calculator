#TreeNode object meant to be implemented for Recursive Descent parsing

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __init__(self, left, right):
        self.val = null
        self.left = left
        self.right = right