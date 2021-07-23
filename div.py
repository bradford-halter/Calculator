from treenode import TreeNode

class Div(TreeNode):
    def __init__(self):
        super().__init__("/")

    def print(self):
        print("(", end ="")
        self.left.print()
        print("/", end ="")
        self.right.print()
        print(")", end ="")

    def eval(self):
        return self.left.eval() / self.right.eval()