from treenode import TreeNode

class Negate(TreeNode):
    def __init__(self, x):
        super().__init__(x, None)

    def print(self):
        print("(", end ="")
        print("-", end ="")
        self.left.print()
        print(")", end ="")

    def eval(self):
        return -self.left.eval()