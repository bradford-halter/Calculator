from treenode import TreeNode

class Integer(TreeNode):
    def __init__(self, x):
        super().__init__(x)

    def print(self):
        print(self.val, end = "")

    def eval(self):
        return self.val