from treenode import TreeNode

# TreeNode Object that stores a left TreeNode, a right TreeNode, and implicitly
# adds the left and right TreeNodes together
#
# left, right => TreeNode which can either be a new expression or a number
#
# print()     => Useful for debugging code and determining order of operations
# eval()      => Returns the quotient of left and right

class Div(TreeNode):
    def __init__(self, left, right):
        super().__init__(left, right)

    def print(self):
        print("(", end ="")
        self.left.print()
        print("/", end ="")
        self.right.print()
        print(")", end ="")

    def eval(self):
        return self.left.eval() / self.right.eval()