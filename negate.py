from treenode import TreeNode

class Negate(TreeNode):
    def __init__(self):
        super().__init__("-")

    def print(self):
        print("(", end ="")
        print("-", end ="")
        self.left.print()
        print(")", end ="")

    def eval(self):
        return -self.left.eval()