from treenode import TreeNode

class Add(TreeNode):
    def __init__(self, left, right):
        super().__init__(left, right)

    def print(self):
        print("(", end ="")
        self.left.print()
        print("+", end ="")
        self.right.print()
        print(")", end ="")

    def eval(self):
        return self.left.eval() + self.right.eval()